# syntehtic data for probability of default
# create and or import into db tables.

import numpy as np
import pandas as pd

# Synthetic LendingClub-style data generator
def generate_credit_data(n_rows=1000, seed=2025):
    np.random.seed(seed)

    data = {
        # Loan Characteristics
        "loan_amnt": np.random.randint(1000, 40000, n_rows),
        "term": np.random.choice(["36 months", "60 months"], size=n_rows, p=[0.7, 0.3]),
        "int_rate": np.round(np.random.normal(13.0, 5.0, n_rows).clip(5, 30), 2),
        "installment": np.round(np.random.normal(400, 150, n_rows).clip(50, 1500), 2),

        # Borrower Demographics
        "emp_length": np.random.choice(
            ["< 1 year", "1 year", "2 years", "3 years", "4 years", 
             "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"],
            size=n_rows, p=[0.05, 0.05, 0.07, 0.07, 0.07, 0.1, 0.1, 0.1, 0.1, 0.09, 0.2]),
        "home_ownership": np.random.choice(["RENT", "MORTGAGE", "OWN", "OTHER"], size=n_rows, p=[0.4, 0.45, 0.13, 0.02]),
        "annual_inc": np.round(np.random.lognormal(mean=10.5, sigma=0.5, size=n_rows).clip(20000, 250000), 0),

        # Credit History
        "dti": np.round(np.random.beta(a=2, b=10, size=n_rows) * 40, 2),  # bounded 0-40
        "fico_range": np.random.randint(600, 800, n_rows),
        "delinq_2yrs": np.random.poisson(0.2, n_rows),
        "inq_last_6mths": np.random.poisson(1, n_rows).clip(0, 8),
        "open_acc": np.random.randint(1, 25, n_rows),
        "total_acc": np.random.randint(5, 80, n_rows),
        "revol_bal": np.random.randint(0, 50000, n_rows),
        "revol_util": np.round(np.random.uniform(0, 150, n_rows), 2),  # utilization can exceed 100%

        # Categorical Loan Info
        "purpose": np.random.choice(
            ["debt_consolidation", "credit_card", "home_improvement", "small_business", "car", "medical", "vacation"],
            size=n_rows, p=[0.55, 0.2, 0.1, 0.05, 0.04, 0.03, 0.03]),
        "verification_status": np.random.choice(["Verified", "Source Verified", "Not Verified"], size=n_rows, p=[0.35, 0.25, 0.4]),
        "addr_state": np.random.choice(["CA", "NY", "TX", "FL", "IL", "NJ", "PA", "OH", "GA", "NC"], size=n_rows),

        # Engineered feature
        "credit_history_length": np.random.randint(1, 40, n_rows),  # years

        # Target Variable (Loan Status)
        "loan_status": np.random.choice(["Fully Paid", "Charged Off", "Current"], size=n_rows, p=[0.7, 0.1, 0.2]),
    }

    return pd.DataFrame(data)


# Example: generate 5 rows
if __name__ == "__main__":
    df = generate_credit_data(n_rows=5)
    print(df)
