#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:56:26 2021

@author: HosungAhn
"""

#%%
def makecsv(filename, Title, PI): 
    import csv
    f = open(filename,"w",encoding='utf-8-sig', newline='')
    wr = csv.writer(f)
    wr.writerow(Title)
    for data in PI:
        wr.writerow(data)
            
    f.close()