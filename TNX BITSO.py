# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:35:24 2022

@author: chief
"""

import requests
import pandas as dt
import json

url = "https://api.bitso.com/v3/trades/?book=btc_mxn"

try:
    respuesta = requests.request( "GET", url )
    PersonasJSON = respuesta.json()

    BTCMXN_bitso = PersonasJSON[ "payload" ]
    grid_BTCMXN_bitso = dt.DataFrame( BTCMXN_bitso )
    
    grid_BTCMXN_bitso.to_excel( "C:/Users/chief/Documents/Proyectos Python/BITSOTxn20221419.xlsx", index=False )
    
    excelEduardo = dt.read_excel( "C:/Users/chief/Documents/Edurdo figueroa.xlsx" )
    
    
except Exception as e: print(e)
