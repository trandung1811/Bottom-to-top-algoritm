#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:08:34 2020

@author: dungtran
"""


### set up environment for simulation
### grid range
grid = [500,500]
#base station location
base_location = [250,250]
  
# number of user 
N_user = 40

# distance between to devices
D = 200

#received power in cellular link
P_u_s = 23

#received power in D2d link
P_u_v = -19

#noise power
N_0 = -176

#Channel bandwidth
B = 10

#carrier frequency
f = 2.5

#interference signal power
P_int = 0

#path loss compensation factor
a = 4

#coefficient link
h = 1
#incentive intensity
c = 100

#fixed amount of data
b = 20

