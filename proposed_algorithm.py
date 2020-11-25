#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:08:34 2020

@author: dungtran
"""

import help_function as hf

def find_max(queue, reward):
    
    max_ = -1
    
    for item in queue:
        if max_ < reward[item]:
            max_ = reward[item]
            item_ = item
    return item_

def tag_element(chain, F_):
    

    for i in range(len(chain)):
        F_[chain[i]] = 1

def free_tag(chain,F_):
    
    for i in range(len(chain)):
        F_[chain[i]] = 0
        
def find_chain(S_fin, chain):
    
    result = []
    
    for item in S_fin: 
        for ele in item: 
            if ele in chain: 
                result.append(item)
                result.append(chain)
                result.append(ele)
                return result
    return result

def split(chain_1, chain_2, key, location, base_location, b):
    
    
    index_1 = chain_1.index(key)
    index_2 = chain_2.index(key)
    sup_chain_1 = chain_1[:index_1]
    sup_chain_2 = chain_2[:index_2]
   
    temp_1 = hf.chain_latency(sup_chain_1, location, base_location, b) + hf.chain_latency(chain_2, location, base_location, b)
    temp_2 = hf.chain_latency(chain_1,location, base_location, b) + hf.chain_latency(sup_chain_2,location, base_location, b)
    if temp_1 > temp_2:
        return chain_1, sup_chain_2
    else: 
        return chain_2, sup_chain_1



def form_chain(location, base_location,vertice, N_user,c, b, F_):
   
    S_fin = []
    T_u = hf.time_latency_to_bs(location, base_location,b)
    for item in T_u:
        chain = {}
        reward = {}
        for i in range(N_user):
            reward[i] = -1
        Queue = []
        if F_[item[0]] != 1:
          
            chain[item[0]] = list([item[0]])
            reward[item[0]] = 0 
            Queue.append(item[0])
            while len(Queue) != 0:
              u = find_max(Queue, reward)
              Queue.remove(u)
              for v in vertice[u]:
             
                   reward_ = hf.calculate_reward(location, base_location, chain[u] ,v,c,b)
                   if reward_ > reward[v]: 
                        reward[v] = reward_
                        temp_chain = chain[u].copy()
                        temp_chain.append(v)
                        chain[v] = temp_chain
                        Queue.append(v)  
            max_ =-1
            key_ = -1
            for key in reward: 
                if reward[key] > max_: 
                    max_ = reward[key]
                    key_ = key
                    
            
          
            result = find_chain(S_fin, chain[key_])
             
            if len(result) != 0:
              
                  chain_1, chain_2 =  split(result[0],result[1], result[2],location, base_location, b)
                  S_fin.remove(result[0]) 
                  free_tag(result[0], F_)
                  S_fin.append(chain_1)
              
                  tag_element(chain_1, F_)
             
                  
            else: 
               tag_element(chain[key_],F_)
               S_fin.append(chain[key_])
                
    return S_fin

def check_f(F_):
    
    for i in range(len(F_)):
        if F_[i] == 0: 
            return False
    return True

def check_chain(S):
    
    for item in S: 
        if len(item) > 1:
            return True
    return False
            
def bottom_to_top_algorithm(location,vertice,N_user,base_location, c, b):

   F_ = {}
   S = []
 
   for i in range(N_user):
       F_[i] = 0
   infi_ = 0
   while infi_ == 0:
       S_fin = form_chain(location, base_location, vertice, N_user, c, b,F_)
       
       if check_chain(S_fin) == False:
           break
       temp_ = S_fin.copy()
       for item in S_fin: 
           if len(item) == 1:
               free_tag(item, F_)
               temp_.remove(item)

       for i in range(N_user):
              
              vertice_ = vertice[i].copy()
              for v in vertice[i]: 
                 
                  if F_[v] == 1:
                      vertice_.remove(v)
              vertice[i] = vertice_
      
           
       for item in temp_: 
           S.append(item)
   for item in S_fin: 
       S.append(item)
   return S
            