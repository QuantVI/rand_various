# -*- coding: utf-8 -*-
### --- This is the Orchestration file

DESCRIPTION = """
The model launcher script
-    reads the run configuration
-    reads cloud/disk locations of model parameters
-    checks/is given locations to save output files
-    does/doesn't call for logging of the process
-    calls model scripts in the order needed to complete the forecast
-    saves output to disk
-    does/doesn't calculate data quality or model performance metrics
-    records full/abbreviated historical run settings/output"""

import a01_set_parameters as paramset
import a02_run_configuration as configset
import a06_run_model as model_engine

path_to_outputs = "/mdl_outputs"

LOGGING = False
CHECK_KPI = False

# params
m_vars = paramset.m_vars
subsids = paramset.ent_enc
# config
cfg = configset.forecast_spec
model_num = cfg["model_number"]
scen_set = configset.set_job_ids(cfg["scenarios"])

# start, run, and stop will handle input processing and output
### We only concern ourselves with handing over
    # - inputs like CONFIG/SCENARIOS and PARAMETERS
    # - a connection or connector for databases
    # - a place to save output as well as what output we want

## STEP - START handle inputs, connection, save location, kpi flag etc
print("|----\tModel Engine Start\t----|")
starting = model_engine.start_model(paramset, configset,
                                    path_to_outputs, CHECK_KPI, LOGGING)
# returns --> dict of pf and mrkt data and params, config, outdir, etc

## STEP - RUN   calls model scripts in the order needed to complete the forecast
print("|----\tModel Engine Run\t----|")

running = model_engine.run_model(starting)
# returns --> lvls, diffs, rwa, market proj, flat market

## STEP - STOP   saves output to disk
print("|----\tModel Engine Stop\t----|")

if CHECK_KPI:
    stopping = model_engine.stop_model(running, path_to_outputs)
    # saves otuputs to disk
    # returns --> kpis

## STEP -    does/doesn't calculate data quality or model performance metrics

measuring = model_engine.measure_model(starting, path_to_outputs)
# runs kpi check and saves its results to disk
# returns --> 1


## STEP -    records full/abbreviated historical run settings/output

parking = model_engine.park_model(starting, running, measuring)
# Potentially save start-run-stop selected data to a historical db
# based on secnario details.
# returns --> 1
