# -*- coding: utf-8 -*-
#### ---- Run Model
# 1. run model
  # Relative change = bond_coeff * B_adjust + equity_coeff * E_adjust
  # Relative change means relative change of the Milan or Margin Volume
  # It is 'estimated' by the regression
  # a. read the config file
  # b. connect to the database
  # c. pull the data according to config DATE
  # d. pivot the data and group by entity
  # e. pass the data needed for the forward projections from DATE
  # f. pull market data from DATE back X months
  # g. transform it (also informs how many old months needed)
  # h. pass transformed market data to formula
  # i. formulate: bring in regression PARAMETERS
  # j. formulate: Param*MkData + Param*MkData = Predict0
  # k. formulate: Predict1 = Real0 * blah of Predict0
  # l. you've created relative prediction series
  # m. pass to func to make absolute prediction series
  # n. created absolute prediction series
  # o. use PARAMS to create FRTB/Basel IV RWA measure and other measures
  # p. apply any needed currency conversion and capping
  # q. output relative and absolute predictions
  # r. output market data and transformations
  # s. run data quality/ KPI checks if flag for this was TRUE

NOTE_02 = """
The transformation is going to be on the market data, which helps
to proxy figure out the new POFTOLIO value. So transformed market data X1
and transformed market data X2 combined + * etc in some way
times some coeffs figured out before... equals the "relative change"
or absolute change in the PORTFOLIO value.
So the next PORTFOLIO values... the one in the future
beyond this months date, is equal to

   coeff_1 * transformed market data x1
+  coeff_2 * transformed market data x2
+  intercept_coeff
== ABS-or-RELATIVE-diff

Then
   Exp (  ABS-or-RELATIVE-diff(n) )   + POFT_at(n-1) = PORTF_at(n)
== EXP (  ABS-or-RELATIVE-diff(n+1) ) + PORTF_at(n)  = PORTF_at(n+1)

I guess we are assuming that the regression equation is trying to predict
the relative difference in the portfolio value between THIS quarter
and the next/future quarter, using market values we can see RIGHT NOW.

Thus
  REL_at(n+1) = diff_of(now vs future) = B1(mrkt trans) + B2(mrkt trans) + B0

where mkrt trans = a transformation of
        CURRENT market data or
        market data at most up to the given rundate/current month"""

NOTE_03 = """
If the main part of the model, this file, can adhere in an abstract way to
having a START -> RUN -> STOP 3-part design, then it will fit a design
that is abstracted and thus interchangeable with any other model.

In essence, all models implement 3 features/methods and the details aren't
really something the orchestrator needs to know about. Here, we try
to divide the rough process into those three parts using the list
from above.
"""

import a01_set_parameters as params
import a02_run_configuration as config
import a04_connect_data as connector

portf_indiv_lvl = """
SELECT
    end_util_amount,
    account_region,
    account_country
FROM portfolio
WHERE date in ({})
"""

markt_base_series = """
SELECT
    ticker1,
    ticker2,
    ticker3
FROM market
WHERE date between '{}' and date_add(date,-12,'m')
"""

markt_proj_series = """
SELECT
    ticker1,
    ticker2,
    ticker3
FROM market_ahead
WHERE

"""

subsid_tree = """
SELECT
    clean_name,
    subsidiary_code,
    corporate_city,
    corporate_region,
    corporate_country,
    primary_regulator
FROM business_entity_Tree
WHERE primary_regulator = 'FINXA'
"""


### --- Model "Engine" process division

## ORCHESTRATOR
# a. read the config file
# - and the parameters file
# pass CONFIG and PARAMS to Engine
# pass KPI flag

## START Engine
# b. connect to the database
# c. pull the PORTF data according to config DATE
# - if KPI flag pull extra PORTF data

def extract_portfolio(some_dates, typ="Portfolio"):
    blurbs = {'a':'Connecting to {} database.\n',
              'b':'Connected to {} database.\n',
              'c':'Disconnected from {} database.\n'}
    
    print(blurbs['a'].format(typ))
    live_conn = connector.conn_to_db(typ)

    print(blurbs['b'].format(typ))
    queried = live_conn.execute(queries["Portf"]["SQL_a"])
    results = queried.to_df()

    live_conn.close()
    print(blurbs['c'].format(typ))

    return results

# f. pull market data from DATE back X months
def extract_market(mvars, some_dates, typ="Market", months_prior=12):
    live_conn = connector.conn_to_db(typ)
    # for a_var in mvars["market"]:
    #    ticker = mvars[avar]
    #    transformations = mvars["stnrty"][a_var] # don't need right now
    #    mq = queries["Markt"]["SQL_a"]
    #    tkr_query = fill_mrkt_query(ticker, mq)
    # use tkr_query instead
    queried = live_conn.execute(queries["Markt"]["SQL_a"])
    results = queried.to_df()

    live_conn.close()
    return results


# i. formulate: bring in regression PARAMETERS
model_params = params.m_vars


## RUN / REV / ACCELERATE Engine
# d. pivot the data and group by entity
scenarios = config.forecast_spec["scenarios"]
raw_pf_data_sets = {s["time_zero"] : extract_portfolio(s["time_zero"])
                    for s in scenarios}
# e. pass the PORTF data needed for the forward projections from DATE
# - forward projections are done to market data first, then propogate to portf
raw_markt_data_sets = {s["time_zero"] : extract_market(s["time_zero"])
                       for s in scenarios}

# g. transform MARKET data it (also informs how many old months needed)
# h. pass transformed market data to formula
mrkt_project = project_market(raw_markt_data_sets, months_forward=12)
mrkt_transf = transf_market(mrkt_project, raw_markt_data_sets, model_params)

# j. formulate: Param*MkData + Param*MkData = Predict0
# k. formulate: Predict1 = Real0 * blah of Predict0
# l. you've created relative prediction series
portf_diffs = project_portf_diffs(raw_pf_data_sets, mrkt_transf)

# m. pass to func to make absolute prediction series
# n. created absolute prediction series
portf_levels = project_portf_lvls(raw_pf_data_sets, portf_diffs)

# o. use PARAMS to create FRTB/Basel IV RWA measure and other measures
# p. apply any needed currency conversion and capping
capped_portf_projs = map(capping [portf_diffs, portf_levels])
cp_portf_diffs, cp_portf_levels = capped_portf_diffs[0],capped_poftf_diffs[1]

rsk_wghtd_assets = cp_portf_levels * [sa_rwa_rate, ima_rwa_rate]

BASE_PORTF_CURR = 'SGD' # for example

mrkt_flatten = mrkt_scen_flat(raw_mrkt_data_sets)

def curr_conv(proj_dict, flat_mrkt=mrkt_flatten):
    for scen in proj_dict:
        if scen["currency"] != BASE_PORTF_CURR:
            scen["lvls"] *= flat_mrkt[scen["currency"]]
            scen["diffs"] *= flat_mrkt[scen["currency"]]

cp_cur_portf_lvls = curr_conv(cp_portf_levels, mrkt_flatten)

cp_cur_portf_diffs = curr_conv(cp_portf_diffs, mrkt_flatten)

cp_cur_portf_raw = curr_conv(rsk_wghtd_assets, mrkt_flatten)

# STOP / DECELERATE Engine
# q. output relative and absolute predictions
save(cp_cur_portf_diffs, to="somediff.csv")
save(cp_cur_portf_lvls, to="somelvls.csv")
save(cp_cur_portf_rwas, to="somerwas.csv")

# r. output market data and transformations
save(mrkt_flatten, to="flathistmarket.csv")
save(mrkt_cen_flat(mrkt_transf), to="flatprojmarket.csv")

# s. run data quality/ KPI checks if flag for this was TRUE
if RUN_KPI:
    kpis = kpi_vs(raw_pf_data_sets,[s["time_zero"] for s in scenarios])

save(kpis, to="keyperformance.csv")


if __name__ == "__main__":
    pass
