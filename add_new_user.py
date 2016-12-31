#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:07:25 2016

@author: victor
"""

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)


def add_new_user(network,new_user,games):
    dicn={'friends':[],'games':games}
    if new_user in network:
        print('The User "',new_user,'" exists already')
    if new_user not in network:
        network[new_user]=dicn

add_new_user(net,'Viti',['Ninja Hamsters','Seven Schemers'])

print(net['Viti'])