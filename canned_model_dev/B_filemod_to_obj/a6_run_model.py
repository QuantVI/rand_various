# -*- coding: utf-8 -*-

#### - OLD VERSION IMPORTS. Reconsider/remove or revamp.
#import a4_connect_data as connector
import a5_get_data_to_model as get_data
import a7_queries as queries
import a8_time_series_manip as tim_ser_mod
import p1_generate_market_projections as project_market

#### ----

class RiskModel:
    def __init__(self, params, config):
        # params is a ModelVariables object
        self.params = params
        # config is a RunConfiguration object
        self.config = config
        # print(self)

    
    def __str__(self):
        str1 = ("|-- A Risk Model with --|\n")
        str2 = (f"{self.params}\n")
        str3 = (f"{self.config}\n")
        #str4 = ("---- ---- ---- ----\n")
        return (str1 + str2 + str3)


    # currency conversion
    def curr_conv(proj_dict, flat_mrkt):
        for scen in proj_dict:
            if scen["currency"] != BASE_PORTF_CURR:
                scen["lvls"] *= flat_mrkt[scen["currency"]]
                scen["diffs"] *= flat_mrkt[scen["currency"]]
        return proj_dict


    # Apply model formula to market data
    # For example a LINEAR REGRESSION formula
    def model_projection(agg_pfs, market_transformed, model_params):
        """
        typ = dif:
            Create relative changes in portfolio, 
            by taking projected market data, and 
            applying the regression equation.
        typ = lvl:
          Create absolute changes in portfolio, by taking
        """
        params = model_params
        mdl_vars = params.m_vars
        mkrt_modif = market_transformed
        # We use the coeffs for each parameter and market data to
        # create a relative move series
        pass

    # NOTE: use this or above for absolute projections
    def lvl_proj(agg_pfs, diff_projections, model_params):
        """We can include a key in the model params for how to go from
        relative changes to level changes. Or we can house the logic here.
        """
        dif_proj = diff_projections
        for proj in dif_proj:
            # fake equation
            level_proj = agg_proj[x] * exp(dif_proj)
        # etc
        pass


    def complex_save(a_kvm, to, fname):
        # kvm means key-value-map. Also know as a dictionary.
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
            print(f"Couldn't save {fname}, due to : {e}")
            return 0

        return 1


    ## START
    def start_model(params, config, outdir, check_kpi, logging):
        ## START Engine        
        scenarios = config.forecast_spec["scenarios"]
        model_params = params.m_vars
        if not check_kpi:
            raw_pf_data_sets = {s["time_zero"] : extract_portfolio(s["time_zero"]) for s in scenarios}
            raw_pfs_for_kpi = ""
        else:
            raw_pfs_for_kpi = ""
            raw_markt_data_sets = {s["time_zero"] : extract_market(s["time_zero"]) for s in scenarios}
        return {"raw_pf_ds": raw_pf_data_sets, "raw_mk_ds": raw_markt_data_sets, "raw_kpi_pfs" : raw_pfs_for_kpi, "params": params, "config":config, "outidr":outdir}


    ## START (redo)
    def start_model(check_kpi=False):
        """
        idea 1: Orchestrator object will call start_model and can
        override defaults for check_kpi and output_directory.

        idea 2: start_model is not running/calling the save function,
        so it doesn't need th take-in the output_directory.

        For KPI checks we assume comparison of current and previous portfolio.
        A possibly external KPI file/function should define how far back
        to pull for the comparison.
        """

        dbObj = get_data.DBCursor()

        # shortending func names from a5_get_data
        pull_portfo = dbObj.extract_portfolio
        pull_market = dbObj.extract_market

        # unmodified portfolio data
        # This should be keyd by job_id since time_zero can is not unique.
        # Thus it doesn't work for a dictionary key.
        memo_pf = {}
        memo_mk = {}
        
        scenarios = self.config["scenarios"]
        
        for s in scenarios:
            # check for portfolio data in the memoization table
            # if not pf data for that date, then pull it.
            # Since time_zero can repeat, we don't want to pull the same data
            # over.
            if not (s["time_zero"] in memo_pf.keys()):
                memo_pf["time_zero"] = pull_portfo(s["time_zero"])
            
            if not (s["time_zero"] in memo_mk.keys()):
                memo_mk["time_zero"] = pull_market(s["time_zero"])

        portf_data_sets = {s["job_id"] : memo_pf(s["time_zero"]) 
                           for s in scenarios}

        

        markt_data_sets = {s["job_id"] : memo_mk(s["time_zero"]) 
                           for s in scenarios}
        
        # datasets from k months ago as comparison
        # shift dates backward
        # pair shifted dates with time_zeroes
        # pull into dictionary indexed by time_zeroes
        if check_kpi: kpi_data_sets = ""

        # It makes sense for this dictionary to be keyed by
        # the time_zero per scenario.
        
        #return {"curr_portfolios" : portf_data_sets,
        #        "prev_portfolios" : kpi_data_sets,
        #        "market_datasets" : markt_data_sets}
        
        # We store the results of the data pulls in the model object
        
        self.curr_portfolios = portf_data_sets
        self.prev_portfolios = kpi_data_sets
        self.market_datasets = markt_data_sets
        # dbObj, a DBCursor from get_data, has functions to use later on
        self.Data_Obj = dbObj


    ## RUN / REV / ACCELERATE Engine
    def run_model(start_model_out):
        pass
        curr_portfo = self.curr_portfolios
        market_data = self.market_datasets
        prev_portfo = self.prev_portfolios
        

        # d. pivot the data and group by entity
        #labeled_pf_data_sets = get_data.label_with_subsidiaries(raw_pf_data_sets)
        #piv1 = get_data.transform_raw_to_pivot_type_1(labeled_pf_data_sets)
        #agg_pf_data_sets = get_data.transform_pivot_type_1_to_entity_level(piv1)
        
        # using Data_Obj
        def LPA(pf_dict):
            """To Label, Pivot, and Aggregate a portfolio with information
            about our subsidiaries."""
            
            labelled = Data_Obj.label_with_subsidiaries(pf_dict)
            pivoted = Data_Obj.transform_raw_to_pivot_type_1(labelled)
            aggreg = Data_Obj.transform_pivot_type_1_to_entity_level(pivoted)
            
            return aggred
        
        # groupby of row-level portfolio data
        cur_pf_agg = LPA(curr_portfo)
        
        if prev_portfo:
            prv_pf_agg = LPA(prev_portfo)
        else:
            prv_pf_agg = ""

        
        
        # The "Model" that projects market data forward is not ours.
        # We merely call it with the right market data and get a forecast.
        
        # g(-2). project raw MARKET data forward
        #mrkt_project = project_market(raw_markt_data_sets, months_forward=12)
        market_forecasts = project_market(market_data, months_forward=12)

        # g(-1). combined projects and raw MARKET data
        #mrkt_past_ftr = time_ser_mod.combine(raw_markt_data_sets, mrkt_project)

        # g. transform MARKET data it (also informs how many old months needed)
        #mrkt_transf = tim_ser_mod.process(params, mrkt_past_ftr)
        market_variants = tim_ser_mod.process(self.params, market_forecasts)
        


        # h. pass transformed market data to formula

        # e. pass the PORTF data needed for the forward projections from DATE
        # j. formulate: Param*MkData + Param*MkData = Predict0
        # k. formulate: Predict1 = Real0 * blah of Predict0
        # l. you've created relative prediction series
        portf_diffs = model_projection(agg_pf_data_sets, mrkt_transf, params)
        
        def relative_change(mrkt_vrnts):
            """
            Parameters
            ----------
            mrkt_vrnts : DICT
                keyed by time_zero date. Each value is the original history
                forecasted forward n-months, or that same series lagged,
                difference, or natual logarithm'd

            Returns
            -------
            The projected relative changes (e.g. month-over-month) of the
            portfolio value. This is done by applying the model equation
            to the (transformed i.e. variants of the) market data.

            """
            #curr_portfo = self.curr_portfolios
            #market_data = self.market_datasets
            #prev_portfo = self.prev_portfolios
            #cur_pf_agg = LPA(curr_portfo)
            #market_forecasts = project_market(market_data, months_forward=12)
            #market_variants = tim_ser_mod.process(self.params, market_forecasts)
                # params is a ModelVariables object
            #self.params = params
                # config is a RunConfiguration object
            #self.config = config

            coe, stn, nam = self.params.m_vars # keys in this dict
            mdl_kvm = self.params.m_vars # the full dict
            
            coeffs = mdl_kvm[coe] # {'equity':1.0,'fxd_inc':0.5, ...}
            stnrty = mdl_kvm[stn] # {'equity':['dif_1','lag_2','ln'], ...}
            mrktnm = mdl_kvm[nam] # {'equity': 'SPX','fxd_inc':'VNGD', ...}
            
            task_pieces = {}
            # task should be a job_id, the key of market_variants
            for task in market_variants:
                pieces = []
                # In each value, we have one time-series per market variable.
                market_variants[task] = curr
                for nm in curr:
                    # each market variable has a time_zero related time-series
                    one_ser_kvm = curr[nm]
                    time_zero = list(one_ser_kvm.keys())[0]
                    one_series = one_ser_kvm[time_zero]
                    # We assume all series have x-months of history, and
                    # (currently y= ) 12-months of projections,
                    # with time_zero being between those. Therefore,
                    # the xth index is the value of the series at time_zero
                    
                    # We explect one number, but use a dict for clarity
                    # this pulls a coefficient depending on if the
                    # param set it as equity, fixed-income, or crypto
                    mult = {nm:coeffs[k] for k in coeffs if mrktnm[k]==nm}
                    mult = mult[nm]
                    
                    # Multiply Coefficient to time_series
                    # Only works if one_series is DataFrame or Series object
                    # If it's a list, * duplicates the list. Insteas use
                    # list( map( lambda x : x*mult, one_series))
                    one_series_mult = one_series * mult
                    
                    # Add this to pieces. Pieces are summed later
                    pieces.append(one_series_mult)
                
                # Add these to the task_piece dictionary by job_id
                task_pieces[task] = pieces
                    

            NOTE01="""Assumed structure of market_variants:
                
                {1234:{"SPX":{"2025-01":dataframe or dict of data and value},
                       "VNGD":{"2025-01":dataframe or dict of data and value},
                       "ETH":{"2025-01":dataframe or dict of data and value}
                       },
                 
                 2468:{"SPX":{"2025-01":dataframe or dict of data and value},
                        "VNGD":{"2025-01":dataframe or dict of data and value},
                        "ETH":{"2025-01":dataframe or dict of data and value}
                        },
                 
                 36912:{"SPX":{"2025-04":dataframe or dict of data and value},
                        "VNGD":{"2025-04":dataframe or dict of data and value},
                        "ETH":{"2025-04":dataframe or dict of data and value}
                        },
                 
                 481216:{"SPX":{"2025-04":dataframe / dict of data & value},
                        "VNGD":{"2025-04":dataframe or dict of data & value},
                        "ETH":{"2025-04":dataframe or dict of data and value}
                        }
                 }
                """



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
  


    ## STOP / DECELERATE Engine
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

        complex_save(kpis, to=a_location, fname="keyperformance.csv")
        # should be multipage xlsx since we can have more than one scenario

        return kpis


    def park_model(eng_start, eng_run, end_measure):
        # Saving outputs to a historical runs db
        # Performing other diagnostics beyond the usual

        # This can thought of as a model_use history
        
        pass

