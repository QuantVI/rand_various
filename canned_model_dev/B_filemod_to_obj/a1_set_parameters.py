# -*- coding: utf-8 -*-

#### ---- Set Model Parameters

class ModelVariables:
    """This is a/the model specification. It holds
    - regression coeffs
    - which market data to pull
    - what transformations to use on the data
    """
    m_info = {"name" : "A Multiple Regression Model",
              "num" : 65535
              }
    
    m_vars = {
        'coeff': {
            'equity':1.0,
            'fxd_inc':0.5,
            'crypto':-0.5
            },
        'stnrty': {
            'equity':['dif_1','lag_2','ln'],
            'fxd_inc':['lag_1'],
            'crypto':['dif_2','ln']
            },
        'market':{
            'equity': 'SPX',
            'fxd_inc': 'VNGD',
            'crypto': 'ETH'
            }
        }
    
    # Entity encoding
    ent_enc = {
    "UK" : "A007",
    "TENBIT" : "T1024",
    "APAC" : "1337",
    "PACMAN" : "Z1900"}

    def __repr__(self):
        str_top = "|- Model Variables -|\n"
        str1 = f" Model Name   : {self.m_info['name']}\n"
        str2 = f" Model Number : {self.m_info['num']}\n"
        return (str_top + str1 + str2)

