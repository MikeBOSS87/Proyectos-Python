# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 05:12:25 2022

@author: chief
"""


from pyzbar.pyzbar import decode
from PIL import Image

try:
    
    fotoQR = Image.open( "C:/Users/chief/Pictures/Socialismo/qrcode.png" )
    ValorQR = decode( fotoQR )
    
    for i in ValorQR:
        print( i.data.decode("utf-8") )
    
except Exception as e: print(e)