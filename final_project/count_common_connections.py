#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 10:03:50 2016

@author: victor
"""

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    cond=((user_A in network) and (user_B in network))
    if cond==False:
        return cond
    if cond==True:
        friends_A=network[user_A]['friends']
        friends_B=network[user_B]['friends']
        common_friends=set(friends_A) & set(friends_B)
        num=len(common_friends)
    return num

print(count_common_connections(net, 'Ollie', 'John'))