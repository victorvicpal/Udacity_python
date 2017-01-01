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
    return len(list_members)

enrollment_num_rows = len(enrollments)             # Replace this with your code
enrollment_num_unique_students = unique_members(enrollments,'account_key')  # Replace this with your code

engagement_num_rows = len(daily_engagement)             # Replace this with your code
engagement_num_unique_students = unique_members(daily_engagement,'acct')  # Replace this with your code

submission_num_rows = len(project_submissions)            
submission_num_unique_students = unique_members(project_submissions,'account_key')  # Replace this with your code


###############################################################################
#################################  Solution   #################################

unique_enrolled_students=set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])
    len(unique_enrolled_students)
