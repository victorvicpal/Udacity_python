#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:52:00 2017

@author: victor
"""
### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

################################# My Solution #################################
def unique_members(table,key):
    list_members=[]
    for i in range(0,len(table)):
        if table[i][key] not in list_members:
            list_members.append(table[i][key])
    return list_members,len(list_members)

enrollment_num_rows = len(enrollments)             # Replace this with your code
enrollment_num_unique_students = unique_members(enrollments,'account_key')[1]
unique_enrollment_members=  unique_members(enrollments,'account_key')[0]# Replace this with your code

engagement_num_rows = len(daily_engagement)             # Replace this with your code
engagement_num_unique_students = unique_members(daily_engagement,'acct')[1]  # Replace this with your code
unique_engagement_members=unique_members(daily_engagement,'acct')[0]

submission_num_rows = len(project_submissions)            
submission_num_unique_students = unique_members(project_submissions,'account_key')[1]  # Replace this with your code
unique_submission_members = unique_members(project_submissions,'account_key')[0]

###############################################################################
#################################  Solution   #################################

#unique_enrolled_students=set()
#for enrollment in enrollments:
#    unique_enrolled_students.add(enrollment['account_key'])
#    len(unique_enrolled_students)

#Change key name from daily_engagement

print(daily_engagement[0].keys())
def change_key(dictionary,new_key,old_key):
    for i in range(0,len(dictionary)):
        dictionary[i][new_key] = dictionary[i][old_key]
        del dictionary[i][old_key]
    return dictionary

change_key(daily_engagement,'account_key','acct')
print(daily_engagement[0].keys())

print(daily_engagement[0]['account_key'])