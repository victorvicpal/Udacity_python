#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:01:49 2016

@author: victor
"""

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    cond=((user_A in network) and (user_B in network))
    if cond==False:
        return cond
    if cond==True:
        if network[user_A]['friends']==[]:
            network[user_A]['friends'].append(user_B)
        else:
            for element in network[user_A]['friends']:
                if user_B in element:
                    return network
                else: network[user_A]['friends'].append(user_B)
        return network
 
#print(add_connection(net,'John','Bryant'))
#add_connection(net, "John", "Freda")
net2 = create_data_structure('')
print(net2)
net2 = add_new_user(net2, 'Alice', [])
print(net2)
net2 = add_new_user(net2, 'Bob', [])
print(net2)
net2 = add_connection(net2, 'Alice', 'Bob')
print(net2)
net2 = add_connection(net2, 'Alice', 'Bob')
print(net2)
print(get_connections(net2, 'Alice'))