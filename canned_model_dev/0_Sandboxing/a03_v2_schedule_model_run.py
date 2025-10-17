# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:03:10 2025
"""

#### ---- Schedule Model Run
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
-    records full/abbreviated historical run settings/output
"""

    # The specific cases to run are in the run config
import a02_run_configuration as configset
    # These are model parameters
import a01_set_parameters as paramset
    # The main model code
import a06_run_model

    # Where should output be saved?
path_to_outputs = "/mdl_outputs"

    # Use logging?
LOGGING = False

# Read/Parse parameters
# We can call params by name.
    # In this area we can create shorthands for the params to reduce
    # length of variable names.
    # e.g. x = configset.dictionary.keyname
m_vars = paramset.m_vars
subsids = paramset.ent_enc

# Read/Parse the specification
    # This is where we can dynamically create the Run ID if needed.
    # This can look at the JSON and create run_ids from the settings.
cfg = configset.forecast_spec
scen_set = configset.set_job_ids(cfg["scenarios"])


### if we think of the model as an engine. Then we should do 3 things
# - start engine
# - run engine
# - stop engine
### If we can design the model-engine that way then any given orchestrator
    # like this file, need not know the specifics of the model.
    # start, run, and stop will handle input processing and output
### We only concern ourselves with handing over
    # - inputs like CONFIG/SCENARIOS and PARAMETERS
    # - a connection or connector for databases
    # - a place to sve output as well as what output we want
## STEP -    calls model scripts in the order needed to complete the forecast

## STEP -    saves output to disk

## STEP -    does/doesn't calculate data quality or model performance metrics

## STEP -    records full/abbreviated historical run settings/output
