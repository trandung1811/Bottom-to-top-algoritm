#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:28:58 2020

@author: dungtran
"""
import matplotlib.pyplot as plt
import random
import parameter as pr
import help_function as hf
import bottom_to_top_algorithm as btt
import proposed_algorithm as new_btt

def set_up_grid(N_user,base_location):
    
    user_location = {}
    
    for i in range(N_user):
        location = []
        location.append(random.randint(0,500))
        location.append(random.randint(0,500))
        user_location[i] = location 
        
   # plt.scatter(base_location[0],base_location[1], color = "Black", s = 80)
   # for item in user_location:
   #     plt.scatter(user_location[item][0], user_location[item][1], color = "green")
    
   # plt.show()
    return user_location

def generate_grap(location, N_user, D):

    vertice = {}
    for i in range(N_user):
        vertice_ = []
        for j in range(N_user):
            if j != i:
                if hf.distance(location[j], location[i]) < D:
                    vertice_.append(j)
        vertice[i] = vertice_
        
    return vertice

def show(location,base_location, N_user, chain):
    
    plt.scatter(base_location[0],base_location[1], color = "Black", s = 80)
    for item in chain:
        if len(item) > 1:
            x = []
            y = []
            for ele in item:
                x.append(location[ele][0])
                y.append(location[ele][1])
            x.append(base_location[0])
            y.append(base_location[1])
            plt.plot(x,y, "-ok")
            
        elif len(item) == 1:
                 plt.scatter(location[item[0]][0], location[item[0]][1], color = "green")
    plt.show()    

       

def compare(chain1, chain2,location, base_location,b):
    
    time_1 = 0
    time_2 = 0
    for item in chain1:
        time_1 += hf.chain_latency(item, location, base_location,b)
    for item in chain2:
        time_2 += hf.chain_latency(item, location, base_location, b)
    return time_1, time_2
def check_total_reduce_time(): 
    
    X = []
    time_1 = []
    time_2 = []
    
    for i in range(200):
         
        user_location = set_up_grid(pr.N_user, pr.base_location)
        vertice = generate_grap(user_location, pr.N_user, pr.D)
        chain_ = btt.bottom_to_top_algorithm(user_location,vertice,pr.N_user, pr.base_location,pr.c,pr.b)
        chain = new_btt.bottom_to_top_algorithm(user_location,vertice,pr.N_user, pr.base_location, pr.c, pr.b)
        t_1, t_2 = compare(chain_, chain, user_location, pr.base_location, pr.b)
        time_1.append(t_1)
        time_2.append(t_2)
        X.append(i)
    total_1 = 0
    total_2 = 0
    for i in range(200): 
        total_1 += float(time_1[i])
        total_2 += float(time_2[i])
    
    plt.plot(X,time_1, label = "total time latency 1")
    plt.plot(X,time_2, label = "total time latency 2")
   
   

    plt.legend()
    plt.show()
def check_the_total_credit(): 
    
    X = []
    cre_1 = []
    cre_2 = []
    for j in range(5,45,5): 
       time_1 = 0
       time_2 = 0
       for i in range(100):
         
          user_location = set_up_grid(pr.N_user, pr.base_location)
          vertice = generate_grap(user_location, pr.N_user, pr.D)
          chain_ = btt.bottom_to_top_algorithm(user_location,vertice,pr.N_user, pr.base_location,pr.c,pr.b)
          chain = new_btt.bottom_to_top_algorithm(user_location,vertice,pr.N_user, pr.base_location, pr.c, pr.b)
          t_1, t_2 = compare(chain_, chain, user_location, pr.base_location, pr.b)
          time_1 = time_1 + t_1*pr.c
          time_2 = time_2 + t_2*pr.c
       cre_1.append(time_1/100)
       cre_2.append(time_2/100)
       X.append(j)
    plt.plot(X,cre_1, label = "total credit 1")
    plt.plot(X,cre_2, label = "total credit 2")

    plt.legend()
    plt.show()

def main():

   #check_the_total_credit()     
    check_total_reduce_time()
        
main()
   
