# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:24:30 2022

@author: 91909
"""
from login import email_val,password_val
import csv
def for_pwd():
    email= input("Enter the Email id: ")
    
    if email_val(email):
        
        with open('user.csv','r') as file:
            reader = csv.reader(file)
            for row in reader:
                if email == row[0]:
                    print('\n Username:'+ email + ' Password '+ row[1])
                    return True
            return False
    else:
       print("please enter valid mail id")