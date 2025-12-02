# This is a faux generator of economic variable / market varibale projections

# Given a set of market data, we assumed it is an ordered time-series,
# and create a number of future values for it.

def project_market(historical_market_data_sets, months_forward):
    # return value needs to contain the history plus the forecast
    fw_months = months_forward
    hmds = historical_market_data_sets
    fmds = {}
    for dataset in hmds:
        future = some_library.project(data=hmds[dataset], steps=fw_months)
        fmds[dataset] = future
    return fmds