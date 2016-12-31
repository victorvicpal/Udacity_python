#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:35:45 2016

@author: victor
"""

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# ----------------------------------------------------------------------------- 
# popularity_games(network): 
#   Function that returns the times a game is liked by the users.
# 
# Arguments: 
#   network: the gamer network data structure
#
# Return: 
#   A dictionary all the video games and the numer of users that likes them.
#   - If the dateset is empty return "no data available"

def popularity_games(network):
    if network=={}:
        return print('No data available')
    video_games={}
    for gamer in network:
        for game in network[gamer]['games']:
            if game not in video_games:
                video_games[game]=1
            else:
                video_games[game]=video_games[game]+1
    return video_games


popular_games=popularity_games(net)


#Popularity Ranking (We sort the games by its values)>>>
import operator
sorted_games = sorted(popular_games.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_games)