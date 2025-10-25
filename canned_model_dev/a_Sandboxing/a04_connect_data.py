# -*- coding: utf-8 -*-
#### ---- Connect Data
#STRS = ["Portfolio","Market"]

STATIC_PARAMS = {
    "Portfolio" : {
        # Portfolio database is a multi-table database,
        # create to simulate a portfolio and aspects of
        # the business related to the portfolio.
        "url": "portf.db",
        "user": None,
        "password": None,
        "pkg": "sqlite"},
    
    "Market" : {
        # Market Data is a dictionary of dataframes,
        # created from a spreadsheet.
        # For now we can store it in sqlite also.
        "url": "market_panel",
        "auth" : "PermitSheet",
        "pkg":"sqlite"}
    }


def db_conn(dbtype, user, key, env_info):
    SETTINGS = STATIC_PARAMS[dbtype]
    pkg = SETTINGS["pkg"]
    
    def sqlite_conn():
        import sqlite3
        return sqlite3.connect(SETTINGS["url"])
    
    def mongo_conn():
        from pymongo import MongoClient
        return MongoClient(
            SETTINGS["host"],
            username=user,
            password=key)
    
    def azurefs_conn():
        from azure.storeage.fileshare import ShareServiceClient
        return ShareServiceClient(
            account_url=SETTINGS["url"],
            credential=key)
    
    make_conn = {"sqlite": sqlite_conn,
                 "mongo" : mongo_conn,
                 "azurefs": azurefs_conn}
    
    if pkg not in make_conn:
        raise ValueError(f"Unsuppoted Database Package: {pkg}")
    
    return make_conn.get(pkg)()


def conn_to_db(dbtype):
    msg = "Enter your"
    str_usern = f"{dbtype} database username"
    str_passw = f"{dbtype} database password"
    
    from m01_AUX_user_input import input_pop_first
    
    u = input_pop_first(message = f"{msg} {str_usern}:\t")
    p = input_pop_first(message = f"{msg} {str_passw}:\t")
    
    return db_conn(dbtype, user=u, key=p, env_info=STATIC_PARAMS)

