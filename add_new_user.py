#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:07:25 2016

@author: victor
"""

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

def add_new_user(network,new_user,games=[]):
    dicn={'friends':[],'games':games}
    if new_user in network:
        print('The User "',new_user,'" exists already')
    if new_user not in network:
        network[new_user]=dicn

add_new_user(net,'Viti',['Ninja Hamsters','Seven Schemers'])


        