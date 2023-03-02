# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:43:38 2022

@author: chief
"""

from io import open

try:
    archivo = open("C:/Users/chief/Documents/BaseGlobalNet.SQL", "r", encoding='utf-8' )

    texto_archivo = archivo.read()
    archivo.close()
    
    
except Exception as e: 
    print(e)