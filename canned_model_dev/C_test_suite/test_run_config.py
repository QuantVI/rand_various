# -*- coding: utf-8 -*-
import os
import sys
# For cross folder imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from B_filemod_to_obj import a2_run_configuration as runconf

import pytest
import copy


# Read the Scenarios for the exercise
spec_1 = runconf.forecast_spec
s = spec_1["scenarios"]
t = copy.deepcopy(s)
t[0]["job_id"] = 0


# Make object
conf_1 = runconf.RunConfiguration()
conf_2 = runconf.RunConfiguration(s)


print("TEST : Set job ids when they are already full of non-false\n")
print(f"ORIGINAL\n\t{s}\n")
print(f"ORIG After set_job_ids\n\t{conf_1.set_job_ids(s)}\n")
print("Set job ids when one is non-false (e.g. 0 or '' or missing\n")
print(f"MODIFIED\n\t{t}\n")
print(f"MOD After set_job_ids\n\t{conf_2.set_job_ids(t)}\n")
