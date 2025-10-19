# -*- coding: utf-8 -*-

## Using the data generators, create synthetic data
## Then import into the sql databases

# This is meant to be a standalone script for database population.
# Thus it does not use any main program files

import sqlite3
import t01_SYNTHETIC_portf_data_for_PD as probdef_data
import t02_SYNTHETIC_portf_data_for_LDG_EAD as lossexp_data


# current file is portf.db . change if necessary.
dbname = "portf.db"

# default rows in each function are 1000.
# We override that here as 10K. change below if needed.
row_count = 10000

probdef_data.
lossexp_data.generate_lgd_ead_data(row_count)

#conn = sqlite3.connect(dbname)
