# -*- coding: utf-8 -*-
# Query Holder

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
