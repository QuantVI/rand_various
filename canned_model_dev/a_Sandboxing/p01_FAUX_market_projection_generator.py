# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 23:26:05 2025
"""

# This is a faux generator of economic variable / market varibale projections

# Given a set of market data, we assumed it is an ordered time-series,
# and create a

def project_market(historical_market_data_sets, months_forward):
    fw_months = months_forward
    hmds = historical_market_data_sets
    fmds = {}
    for dataset in hmds:
        future = some_library.project(data=hmds[dataset], steps=fw_months)
        fmds[dataset] = future
    return fmds
