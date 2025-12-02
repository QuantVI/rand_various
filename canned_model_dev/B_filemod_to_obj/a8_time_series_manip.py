# -*- coding: utf-8 -*-

#### ---- Market Data Transformations

def lag(thiseries, thismuch):
    pass

def diff(thisseries, thismuch):
    pass

def logarithm(thisseries, thisbase):
    pass

def process(parameter_set, market_data):
    market_vars_kvm = parameter_set["market"]
    modifs = parameter_set["stnrty"]

    # match the var with its modifications
    # modifs assume to be in order
    # for each modification call the appor function
    #   differencing
    #   lagging
    #   logarithm
    # return finalized modified time series
    variants = 1 # contians historical, forecasted, and transformed
    return variants

def combine(historical_market_data_kvm, projected_market_data_kvm):
    hist = historical_market_data_kvm
    future = projected_market_data_kvm

    new_series = {}
    for scen_date_h, scen_date_f in zip(hist,future):
        h = hist[scen_date_h]
        f = future[scen_date_f]
        if scen_date_h == scen_date_f:
            new_series[scen_date] = h.append(f)
        else:
            raise Exception("Future key not aligned with historical key",
                            f"hist: {scen_date_h}, fut: {scen_date_f}")
    return new_series
