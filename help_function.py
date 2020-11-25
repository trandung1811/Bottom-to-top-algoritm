#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:08:34 2020

@author: dungtran
"""

import math
import parameter as pr

def distance(x,y):

    return math.sqrt((y[1] - x[1])* (y[1] - x[1]) + (y[0] - x[0])*(y[0] - x[0]))

def data_rate_to_device(location_1, location_2):
    return math.log2(1+ ((pr.P_u_v *(distance(location_1, location_2)**-2))/pr.N_0))

def data_rate_to_BS(location, N_user, base_location):
    
    data_rate_to_bs = {}
    for i in range(N_user):
        data_rate_to_bs[i] = math.log2(1+ ((pr.P_u_s *(distance(location[i], base_location)**-2))/pr.N_0))

    return data_rate_to_bs  

def time_latency_to_bs(location,base_station, b):

    T_u = {}
    for i in range(len(location)):
        T_u[i] = b/data_rate_to_device(location[i], base_station)

    new_T_u = sorted(T_u.items(), key=lambda x: x[1], reverse=True)

    return new_T_u

def chain_latency(chain,location, base_location, b):
    
    n = len(chain)
    T_s = 0
    for i in range(n-1):
        for j in range(i):
           
            T_s = T_s + 20/3*(b/data_rate_to_device(location[chain[i]], location[chain[j]]))
    for i in range(n):
        T_s = T_s + 10/6*b/data_rate_to_device(location[chain[-1]], base_location)
    
    return T_s

def calculate_reward(location, base_location, chain,vertice, C, b):
    
    T_s = chain_latency(chain, location, base_location, b)
    new_chain = chain.copy()
    new_chain.append(vertice)
    T_s_ = chain_latency(new_chain, location, base_location, b)
    
    return C*(T_s - T_s_)
    
   
