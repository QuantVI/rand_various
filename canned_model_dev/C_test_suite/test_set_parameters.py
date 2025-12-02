import os
import sys

# For cross folder imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from B_filemod_to_obj import a1_set_parameters

import pytest

# Create oject
m = a1_set_parameters.ModelVariables()
# see the Entity Encodings
print(m.ent_enc)
# see Model Variables
print(m.m_vars)
