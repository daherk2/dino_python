# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:33:15 2016

@autor: fabio
"""


from __future__ import division
import pyautogui
import time
import pyscreenshot as ImageGrab
from PIL import Image

time.sleep(5)
c = 0
while(True):
    im=ImageGrab.grab(bbox=(437,227,490,316)) # X1,Y1,X2,Y2
    #old new value im=ImageGrab.grab(bbox=(425,215,448,304)) # X1,Y1,X2,Y2    
    #im=ImageGrab.grab(bbox=(425,225,448,245))          
    im.save('img'+str(c)+'.png')
    image_file = Image.open("img"+str(c)+".png")
    #image_file= image_file.convert('L')
    image_file = image_file.convert('1')
    histo = image_file.histogram()
    histo_string = ''
    histo[:] = (value for value in histo if value != 0)  
    print histo
    if int(histo[0]) > 170:
         pyautogui.press('up')
         print ('jump '+str(histo[0]))
    else:
        #pyautogui.press('down')
        print ('stopped'+str(histo[0]))
    image_file.save('img'+str(c)+'.png')
    #c = c + 1


