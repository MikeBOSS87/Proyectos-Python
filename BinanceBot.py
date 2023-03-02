# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 03:02:48 2022
 
Basic API for reading/writing single-read fast5 files.
"""

import io

try:
    foto = io.open("C:/Users/chief/Pictures/Socialismo/HilePepi.jpg", "rb", buffering = 0)
    print( foto.read() )

except Exception as e: print(e)