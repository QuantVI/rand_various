# -*- coding: utf-8 -*-
#### ---- Run Model
#import a01_set_parameters as params
#import a02_run_configuration as config
import a04_connect_data as connector

import a05_v2_get_data_to_model as get_data
from a05_v2_get_data_to_model import extract_portfolio as extract_portfolio
from a05_v2_get_data_to_model import extract_market as extract_market

import a07_v1_queries as queries
import a08_v1_time_series_manip as tim_ser_mod

import p01_FAUX_market_projection_generator as project_market

#LOGGING = True
#CHECK_KPI = True

### --- Model "Engine" process division

## defs used in START-RUN-STOP process
def curr_conv(proj_dict, flat_mrkt=mrkt_flatten):
    for scen in proj_dict:
        if scen["currency"] != BASE_PORTF_CURR:
            scen["lvls"] *= flat_mrkt[scen["currency"]]
            scen["diffs"] *= flat_mrkt[scen["currency"]]
    return proj_dict

def diff_proj(agg_pfs, market_transformed, model_params):
    """
    typ = dif:
      Create relative changes in portfolio, by taking projected
      market data, and applying the regression equation.

    typ = lvl:
      Create absolute changes in portfolio, by taking
    

    """
    params = model_params
    mdl_vars = params.m_vars
    mkrt_modif = market_transformed
    # We use the coeffs for each parameter and market data to
    # create a relative move series
    pass

def lvl_proj(agg_pfs, diff_projections, model_params):
    """We can include a key in the model params for how to go from
    relative changes to level changes. Or we can just house the logic here.
    """
    dif_proj = diff_projections
    for proj in dif_proj:
        # fake equation
        level_proj = agg_proj[x] * exp(dif_proj)
    # etc
    pass

def complex_save(a_kvm, to, fname):
    # kvm meand key-value-map. Also know as a dictionary.
    from pandas import DataFrame
    for some_key in a_kvm:
        if a_kvm[some_key].isinstanceof(list):
            pass
        if a_kvm[some_key].isinstanceof(dict):
            pass
        if a_kvm[some_key].isinstanceof(DataFrame):
            pass
    # turn all into multisheet xls
    try:
        pass
    except Exception as e:
        print(f"Couldn't save {}, due to : {e}")
        return 0

    return 1


## ORCHESTRATOR
# a. read the config file
# - and the parameters file
# pass CONFIG and PARAMS to Engine
# pass KPI flag

## START
def start_model(params, config, outdir, check_kpi, logging):
    ## START Engine
    #globals()["LOGGING"] = logging
    #globals()["CHECK_KPI"] = check_kpi
    
    scenarios = config.forecast_spec["scenarios"]
    # i. formulate: bring in regression PARAMETERS
    model_params = params.m_vars
    
    # b. connect to the database
    # c. pull the PORTF data according to config DATE
    #    If KPI flag, pull extra PORTF data
    if not check_kpi:
        raw_pf_data_sets = {s["time_zero"] : extract_portfolio(s["time_zero"])
                            for s in scenarios}
        raw_pfs_for_kpi = ""
    else:
        # pull portf raw data for all time_zero-N months
        # store this in a dict by time zero (i.e. 1 per unique time-zero)
        # changes between months used in kpi
        raw_pfs_for_kpi = ""

    # f. pull market data from DATE back X months
    raw_markt_data_sets = {s["time_zero"] : extract_market(s["time_zero"])
                           for s in scenarios}

    return {"raw_pf_ds": raw_pf_data_sets,
            "raw_mk_ds": raw_markt_data_sets,
            "raw_kpi_pfs" : raw_pfs_for_kpi,
            "params": params,
            "config":config,
            "outidr":outdir}
            

## RUN / REV / ACCELERATE Engine
def run_model(starting_output_kvm):
    pass
    raw_pf_data_sets = starting_output_kvm["raw_pf_ds"]
    raw_markt_data_sets = starting_output_kvm["raw_mk_ds"]
    params = starting_output_kvm["params"]

    # d. pivot the data and group by entity
    labeled_pf_data_sets = get_data.label_with_subsidiaries(raw_pf_data_sets)
    piv1 = get_data.transform_raw_to_pivot_type_1(labeled_pf_data_sets)
    agg_pf_data_sets = get_data.transform_pivot_type_1_to_entity_level(piv1)

    # g(-2). project raw MARKET data forward
    mrkt_project = project_market(raw_markt_data_sets, months_forward=12)

    # g(-1). combined projects and raw MARKET data
    mrkt_past_ftr = time_ser_mod.combine(raw_markt_data_sets, mrkt_project)

    # g. transform MARKET data it (also informs how many old months needed)
    mrkt_transf = tim_ser_mod.process(params, mrkt_past_ftr)

    # h. pass transformed market data to formula

    # e. pass the PORTF data needed for the forward projections from DATE
    # j. formulate: Param*MkData + Param*MkData = Predict0
    # k. formulate: Predict1 = Real0 * blah of Predict0
    # l. you've created relative prediction series
    portf_diffs = diff_proj(agg_pf_data_sets, mrkt_transf, params)

    # m. pass to func to make absolute prediction series
    # n. created absolute prediction series
    portf_levels = lvl_proj(agg_pf_data_sets, portf_diffs, params)

    
    # p. apply any needed  capping
    
    capped_portf_projs = map(capping [portf_diffs, portf_levels])
    cp_portf_diffs = capped_portf_projs[0]
    cp_portf_levels = capped_portf_projs[1]

    # o. use PARAMS to create FRTB/Basel IV RWA measure and other measures
    rsk_wghtd_assets = cp_portf_levels * [sa_rwa_rate, ima_rwa_rate]

    # p(1). apply any needed currency conversion
    BASE_PORTF_CURR = 'SGD' # for example

    mrkt_flatten = mrkt_scen_flat(raw_mrkt_data_sets)

    cp_cur_portf_lvls = curr_conv(cp_portf_levels, mrkt_flatten)
    cp_cur_portf_diffs = curr_conv(cp_portf_diffs, mrkt_flatten)
    cp_cur_portf_rwa = curr_conv(rsk_wghtd_assets, mrkt_flatten)

    return {"pf_levels": cp_cur_portf_lvls,
            "pf_diffs": cp_cur_portf_diffs,
            "pf_riskwa": cp_cur_portf_rwa,
            "mod_mrkt_proj": mrkt_transf,
            "flat_mrkt_raw": mrkt_flatten}


# STOP / DECELERATE Engine
def stop_model(running_output_kvm, out_dir):
    kvm = running_output_kvm
    # q. output relative and absolute predictions
    complex_save(kvm["pf_diffs"], to=out_dir, fname="somediff.csv")
    complex_save(kvm["pf_levels"],to=out_dir, fname="somelvls.csv")
    complex_save(kvm["pf_riskwa"],to=out_dir, fname="somerwas.csv")

    # r. output market data and transformations
    complex_save(kvm["flat_mrkt_raw"], to=out_dir, fname="flathistmrkt.csv")
    complex_save(kvm["mod_mrkt_proj"], to=out_dir, fname="flatprojmrkt.csv")

    return 1

def measure_model(start_output_kvm, a_location):
    # s. run data quality/ KPI checks if flag for this was TRUE
    #if RUN_KPI: <-- already checked in orchestrator

    # this can be run on agg_pf_data_sets
    # otherwise it likely does the entity aggregation again
    scen_pfs = start_output_kvm["raw_pf_ds"]
    old_pfs = start_output_kvm["raw_kpi_pfs"]

    kpis = kpi_vs(scen_pfs, old_pfs)
    # returns 1 dataframe er scenario with rows for each kpi tested

    complex_save(kpis, to=a_location fname="keyperformance.csv")
    # should be multipage xlsx since we can have more than one scenario

    return kpis


def park_model(eng_start, eng_run, end_measure):
    # Saving outputs to a historical runs db
    # Performing other diagnostics beyond the usual

    # This can thought of as a model_use history

if __name__ == "__main__":
    pass
