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
the transformation is going to be on the market data, which help to proxy figure out the new POFTOLIO value. Sp transformed market data X1 and transformed market data X2 combined + * etc in some way
times some coeffs difured out before... equals the "relative change" or absolute change
in the PORTFOLIO value. So the next PORTFOLIO values.. the one in the future beyond this months date, is equal to

coeff_1 * transformed market data x1 + coeff_2 * transformed market data x2 + intercept_coeff
=== ABS-or-RELATIVE-diff

Then  Exp (  ABS-or-RELATIVE-diff(n) ) + POFT_at(n-1) = PORTF_at(n)
=== EXP (  ABS-or-RELATIVE-diff(n+1) ) + PORTF_at(n) = PORTF_at(n+1)

I guess we are assuming that the regression equation is trying to predict the relative difference in the portfolio value between THIS quarter an the next/future quarter, using market value we can see RIGHT NOW.

Thus REL_at(n+1) = diff_of(now vs future) = B1(mrkt trans) + B2(mrkt trans) + B0
	where mkrt trans = a transformation of CURRENT market data or market data at most
	up to the given rundate/current month
"""

NOTE_03 = """
If the main part of the model, this file, can adhere in an abstract way to
having a START -> RUN -> STOP 3-part design, then it will fit a design
that is abstracted and thus interchangeable with any other model.

In essence, all models implement 3 features/methods and the details aren't
really something the orchestrator needs to know about. Here, we try
to divide the rough process into those three parts using the list
from above.
"""

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



    # Either here or in get_data_to_model we establish a connection
    # get_data_to_model should also have the required query/queries
    # PARAMS tell us which time-series/asset/ticker to pull
    # no transformation.
    # We can have a separate call to a generator for forecasts of
    # the market data.

### --- Model "Engine" process division

  # Relative change = bond_coeff * B_adjust + equity_coeff * E_adjust
  # Relative change means relative change of the Milan or Margin Volume
  # It is 'estimated' by the regression

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
    # Messages to print to screen
    blurbs = {'a':'Connecting to {} database.\n',
              'b':'Connected to {} database.\n',
              'c':'Disconnected from {} database.\n'}
    
    print(blurbs[a].format(typ))
    # Create connection to db for portfolio information
    # All settings are in the connection code file.
    live_conn = connector.conn_to_db(typ)
    print(blurbs[b].format(typ))
    # use conn object to execute query
    queried = live_conn.
		# what is the query. go get it
        # what params need to be put into the query text

    # Get query results
    # Close conn
    # Done with portfolio data extraction
    live_conn.close()
    print(blurbs[c].format(typ))
    # ---- return raw query results
    return 1 # this should be the raw portf data


  # f. pull market data from DATE back X months
def extract_market(some_dates,typ="Market",months_prior=12):
    live_conn = connector.conn_to_db(typ)

  # i. formulate: bring in regression PARAMETERS

## RUN / REV / ACCELERATE Engine
  # d. pivot the data and group by entity
  # e. pass the PORTF data needed for the forward projections from DATE  

  # g. transform MARKET data it (also informs how many old months needed)
  # h. pass transformed market data to formula

  # j. formulate: Param*MkData + Param*MkData = Predict0
  # k. formulate: Predict1 = Real0 * blah of Predict0
  # l. you've created relative prediction series
  
  # m. pass to func to make absolute prediction series
  # n. created absolute prediction series
  
  # o. use PARAMS to create FRTB/Basel IV RWA measure and other measures
  # p. apply any needed currency conversion and capping

# STOP / DECELERATE Engine
  # q. output relative and absolute predictions
  # r. output market data and transformations
  # s. run data quality/ KPI checks if flag for this was TRUE

if __name__ == "__main__":
    # Think of this as things that need to happen outside of this script
    # in order to run the items above.
    import a01_set_parameters as paramset
    import a02_run_configuration as configset
    import a04_connect_data as connector
