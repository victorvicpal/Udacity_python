#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:31:59 2016

@author: victor
"""

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    new_list=[]
    if user not in network:
        return None
    if user in network:
        if network[user]['friends']==[]:
            return new_list
        else: 
            for element in network[user]['friends']:
                sub=network[element]['friends']
                for conn in sub:
                    #if ((conn not in new_list) and (conn not in network[user]['friends']) and conn!=user):
                     if conn not in new_list:
                        new_list.append(conn)
    return new_list

print(get_connections(net,'Bryant'))
print(get_secondary_connections(net, 'Bryant'))

