# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 09:45:51 2022

@author: Simon
"""

from rembg import remove
from PIL import Image
input_path=''
output_path='output.png'
input= Image.open(input_path)
output= remove(input)
output.save(output_path)