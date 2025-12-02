# synthetic data for LGD and EAD

import pandas as pd
import numpy as np


NOTE_01 = """
--------
## LGD (Loss Given Default)

LGD is:

    $$
    LGD = \frac{\text{EAD – Recovery}}{\text{EAD}}
    $$

Columns to use should describe **recoveries vs. what was owed**:

* **`out_prncp` / `out_prncp_inv`** → Outstanding principal at the time of default.
* **`total_rec_prncp`** → Total principal received.
* **`total_rec_int`** → Total interest received.
* **`total_rec_late_fee`** → Total late fees received.
* **`recoveries`** → Amount recovered post-default (collection).
* **`collection_recovery_fee`** → Fees deducted from recoveries.
* **`loan_amnt`** (or `funded_amnt`) → Original exposure, needed for scaling.
* **`loan_status`** → Indicator of whether default/charged-off (used to identify LGD cases).


**Characteristics:**

* LGD columns are typically **monetary** (dollar amounts).
* For defaults, LGD often lies between **0.2 and 0.9** depending on recoveries.
* Recoveries tend to be **skewed right** (most loans recover little, a few recover a lot).


--------
## EAD (Exposure at Default)

EAD is:

    $$
    EAD = \text{Exposure value at the time of default}
    $$

For installment loans, this means **the remaining balance when default occurs**:

* **`out_prncp`** → Directly used as EAD if default occurs.
* **`funded_amnt`** / **`loan_amnt`** → Original notional, for scaling.
* **`revol_bal`** (if revolving loans) → Current revolving balance.
* **`revol_util`** → Utilization percentage, sometimes used in proxy EAD models.
* **`total_pymnt` / `total_pymnt_inv`** → Useful for tracking how much was paid before default.

**Characteristics:**

* For amortizing loans, EAD **declines over time** as installments are paid.
* For revolving loans, EAD **depends on utilization**.
* Usually modeled as a fraction of original exposure, e.g. `EAD = CCF * Exposure` (where CCF = credit conversion factor).

--------
## Summary Table

| Category | Columns (LendingClub style)                                                                                                   | Role                                      | Characteristics                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------- |
| LGD      | `out_prncp`, `total_rec_prncp`, `total_rec_int`, `total_rec_late_fee`, `recoveries`, `collection_recovery_fee`, `loan_status` | Needed to compute cash flows vs. exposure | Skewed, recoveries usually low                      |
| EAD      | `out_prncp`, `funded_amnt`, `loan_amnt`, `revol_bal`, `revol_util`, `total_pymnt`, `total_pymnt_inv`                          | Balance outstanding at default            | Declining (installments) or usage-based (revolving) |

---

In practice, for **synthetic generation**:

* **LGD**:  you’d simulate recoveries as a fraction of exposure
            (Beta distribution is common).
* **EAD**:  you’d simulate balance as a function of time-to-default
            and loan type.

---

Do you want me to sketch a **dummy generator** that:

* Creates EAD as a declining balance process,
* Creates LGD as (1 – recovery\_rate) with recovery\_rate sampled from
    a Beta distribution?
"""


risk_columns = {
    "LGD": [
        "recoveries",
        "collection_recovery_fee",
        "last_pymnt_d",
        "last_pymnt_amnt",
        "total_rec_prncp",
        "total_rec_int",
        "total_rec_late_fee",
        "last_credit_pull_d"
    ],
    "EAD": [
        "funded_amnt",
        "loan_amnt",
        "out_prncp",
        "revol_bal",
        "revol_util"
    ]
}


def generate_lgd_ead_data(n_rows=1000, random_state=2025):
    np.random.seed(random_state)

    # # # - - - Exposure at Default (EAD) - - - # # #
    # loan_amt is the funded loan amount
    loan_amnt = np.random.randint(1000, 40000, n_rows)
    # funded_amnt is close to loan_amnt
    funded_amnt = loan_amnt + np.random.randint(-500, 500, n_rows)
    # Make sure funded_amnt is nonnegative
    funded_amnt = np.clip(funded_amnt, 500, None)
    # Outstanding principle is between 0 and funded_amnt
    out_prncp = np.random.uniform(0, funded_amnt)
    # revolving balance (i.e. for credit cards or Lines, not loans)
    revol_bal = np.random.randint(0, 50000, n_rows)
    # utilization ratio %
    revol_util = np.random.uniform(0, 150, n_rows)


    # # # - - - Loss Given Default - - - # # #
    # Recovery is skewed, and often small
    recoveries = np.random.exponential(scale=200, size=n_rows)
    # Recovery can't exceed principal
    recoveries = np.clip(recoveries, 0, out_prncp)
    # small fraction
    collection_recovery_fee = np.random.uniform(0, recoveries / 2)
    # Amount of the last payment made
    last_pymnt_amnt = np.random.uniform(0, 2000, n_rows)
    # principal repaid
    total_rec_prncp = funded_amnt - out_prncp
    # interest repaid
    total_rec_int = np.random.uniform(0, funded_amnt * 0.3)
    # late fees
    total_rec_late_fee = np.random.uniform(0, 100, n_rows)

    # # # - - - Optional Columns - - - # # #
    # Disbaled, or not included in final df for now

    ## issue_d_arr ==> loan origination date
    ## last_pymnt_d_Arr ==> last payment date
    ## last_credit_pull_d_arr ==> last time bureau info was pulled

    # Create issue date (loan origination)
    issue_dates = pd.date_range(start="2010-01-01",
                                end="2018-12-31", freq="M")
    issue_d_arr = np.random.choice(issue_dates, size=n_rows)

    # Last payment date must be after issue date
    offset_days = np.random.randint(30, 365*5, size=n_rows)
    last_pymnt_d_arr = issue_d_arr + pd.to_timedelta(offset_days, unit="D")

    # Credit pull date can be before or after issue
    sdt, edt = "2009-01-01", "2019-12-31"
    credit_pull_dates = pd.date_range(start=sdt, end=edt, freq="M")
    last_credit_pull_d_arr = np.random.choice(credit_pull_dates, size=n_rows)


    # Build DataFrame
    df = pd.DataFrame({
        "loan_amnt": loan_amnt,
        "funded_amnt": funded_amnt,
        "out_prncp": out_prncp,
        "revol_bal": revol_bal,
        "revol_util": revol_util,
        "recoveries": recoveries,
        "collection_recovery_fee": collection_recovery_fee,
        "last_pymnt_amnt": last_pymnt_amnt,
        "total_rec_prncp": total_rec_prncp,
        "total_rec_int": total_rec_int,
        "total_rec_late_fee": total_rec_late_fee
        ## -- can include date columns here
        #"issue_d" : issue_d_arr,
        #"last_pymnt_d" : last_pymnt_d_arr,
        #"last_credit_pull_d" : last_credit_pull_d_arr
    })

    return df


if __name__ == "__main__":
    df_lgd_ead = generate_lgd_ead_data(n_rows=10)
    print(df_lgd_ead.head())


## Can use these for df binding
# lgd_df = df[risk_columns["LGD"]]
# ead_df = df[risk_columns["EAD"]]

EXAMPLE = """
df_main = ... # data we download or generate for finding PD
df_lgd_ead = generate_lgd_ead_data(n_rows=len(df_main))

# Join such that we add more columns.
df_full = pd.concat([df_main, df_lgd_ead], axis=1)
"""
