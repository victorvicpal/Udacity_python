#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:28:18 2017

@author: victor
"""

#print(unique_enrollment_members,unique_engagement_members,unique_submission_members)
def not_in_table(list1,list2):
    new_list=[]
    for element in list2:
        if element not in list1:
            new_list.append(element)
    return new_list
    
missing_values=not_in_table(unique_engagement_members,unique_enrollment_members)
print(missing_values)


def find_problems(dictionary,missing):
    n=0
    for j in range(0,len(dictionary)):
        for i in range(0,len(missing)):
            if dictionary[j]['account_key']==missing[i]:
                if dictionary[j]['join_date']!=dictionary[j]['cancel_date']:
                    n+=1
                    print(dictionary[j])
    return n

print(find_problems(enrollments,missing_values))




        

