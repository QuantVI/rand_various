# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:03:10 2025
"""

#### ---- Schedule Model Run

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

import a01_set_parameters as paramset
import a02_run_configuration as configset


path_to_model = "/" # instead we will import the main model code
path_to_spec = "/" # the specific cases to run are in the run config
path_to_metadata_parameters = "/" # this is in the set_parameters file

# Where should output be saved?
path_to_outputs = "/mdl_outputs"

# Use logging?
LOGGING = False

import path_to_model # this will move above, and the var removed

# Read/Parse parameters
configset.get_params() # we don't need this we can call params by name
    # in this area we can create shorthands for the params to reduce
    # the variable names
    # e.g. x = configset.dictionary.keyname

# Read/Parse the specification
    # We might not need this. However, this is where we can dynamically
    # create the Run ID
# This will look at the JSON and create run_ids from the settings
run_set = configset.create_run_set

# This will
run_ids = list(run_set.keys())