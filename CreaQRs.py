# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 05:35:08 2022

@author: chief
"""

import qrcode
from PIL import Image

try:
    qr = qrcode.QRCode( 
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )

    qr.add_data( "JBOSS Admin MikeBOSS0609874915 M!k3BOSS06098725014915 183742" )
    qr.make( fit = True )
    
    img = qr.make_image( fill_color = "black", back_color = "white" )
    img.save( "C:/Users/chief/Pictures/Socialismo/CodigoQR.png" )
    
except Exception as e: print(e)