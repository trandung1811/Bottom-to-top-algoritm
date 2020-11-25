#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:08:34 2020

@author: dungtran
"""

import help_function as hf


def bottom_to_top_algorithm(location,vertice,N_user,base_location, c, b):

   
    F_ = {}
    S_fin = []
    for i in range(N_user):
        F_[i] = 0
    T_u = hf.time_latency_to_bs(location, base_location,b)
   
    for item in T_u:
        chain = []
        Queue = []
        if F_[item[0]] != 1:
            chain.append(item[0])
            F_[item[0]] = 1
            Queue.append(item[0])
            while len(Queue) != 0: 
              u = Queue[0]
              del Queue[0]
              uti = 0
              current_device = None
              for v in vertice[u]:
                   if F_[v] !=1:
                       reward = hf.calculate_reward(location, base_location, chain,v,c,b)
                       if reward > uti: 
                           uti = reward 
                           current_device = v 
                           
              if uti == 0: 
                  break
              else:
                
                 chain.append(current_device)
                 F_[current_device] = 1
                 Queue.append(current_device)    
              
        S_fin.append(chain)      
    return S_fin
            
        
                        
