# -*- coding: utf-8 -*-

import a4_connect_data as connector
import a7_queries as queries

#### ---- Get data to Model

# After connect to the db, we run various commands.
class DBCursor:
    """Object creates db connection
    Then the object uses the connection to extract data from whatever
    source it is, and does basic transformations if needed.
    """
    def __init__(self):
        pass


    def extract_portfolio(self, some_dates, typ="Portfolio"):
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


    def extract_market(self, mvars, some_dates, 
                       typ="Market", months_prior=12):
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


    # Used for Portfolio Data
    def label_with_subsidiaries(): pass


    # Used for Portfolio Data
    def transform_raw_to_pivot_type_1(): pass


    # Used for Portfolio Data
    def transform_pivot_type_1_to_entity_level(): pass


    # ----------------------------------------
    # given a database connection, run the instructions to retrieve data
    def extract_portf_data(a_connection, some_dates, some_instructions):
        # We're AWARE this is q sqlite db. We run command accordingly.
        # Instructions are grouped elsewhere, for easier updating later.
        cur = a_connection.cursor()
    
        if KPI_ALSO:
            pass
            "change, for example, the data range"
        
        in_i = some_instructions[0]
        in_i_full = in_i.format(*some_dates)
        
        cur.execute


# ----------------------------------------
# Portfolio Instructions

# This month's portfolio
Port_from_a_to_b = """
    select * from account_level as acc 
    where acc.cur_bal_date in ({dt1},{dt2})
    """
# account_level can have 
    # 1 row per account per month: YYYY-MM-DD, or
    # 1 row per account per day: YYYY-MM-DD
    # Therefore, selecting by a full date ensures 1 row per account
# DEDUPLICATION of records is the job/responsibility of the team(s)
# that manage such tables, who are likely in a different department.
# As such duplication should not be managed directly. 
# Rather, if found it's reported.
# ----------------------------------------
