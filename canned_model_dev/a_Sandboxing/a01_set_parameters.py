# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 13:49:00 2025
"""

#### ---- Set Model Parameters

    # this is the model speficiation like regresios coeffs
    # which market data to pull, and how much to lag it by etc

# Model Variables
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
    "PACMAN" : "Z1900"
    }
