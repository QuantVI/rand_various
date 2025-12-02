import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from B_filemod_to_obj import a_set_parameters


print(os.path.abspath(__file__))
print()
print("\n".join(sys.path))
"""
'C:\\Users\\RyzenKaisen\\Documents\\GitHub\\rand_various\\canned_model_dev\\C_test_suite', 
'C:\\Users\\RyzenKaisen\\anaconda3\\python39.zip', 

'C:\\Users\\RyzenKaisen\\anaconda3\\DLLs', 
'C:\\Users\\RyzenKaisen\\anaconda3\\lib', 'C:\\Users\\RyzenKaisen\\anaconda3', 

'C:\\Users\\RyzenKaisen\\anaconda3\\lib\\site-packages', 

'C:\\Users\\RyzenKaisen\\anaconda3\\lib\\site-packages\\locket-0.2.1-py3.9.egg', 

'C:\\Users\\RyzenKaisen\\anaconda3\\lib\\site-packages\\win32', 

'C:\\Users\\RyzenKaisen\\anaconda3\\lib\\site-packages\\win32\\lib', 

'C:\\Users\\RyzenKaisen\\anaconda3\\lib\\site-packages\\Pythonwin']
"""