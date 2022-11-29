# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:29:07 2022

@author: 91909
"""
from login import email_val,password_val
import csv
from forgetpass import for_pwd
def reg():
    email= input("Enter the Email id: ")
    

    if email_val(email):
        password = input("Enter the password : ")
        if password_val(password):
                with open('user.csv','a',newline='') as file:
                    
                    file.writelines(email +","+ password)
                    file.write('\n')
                    file.close()
                    print("Registration sucessfully")
                return True
        else:
                print("Password Not Valiadte")
    else:
           print("Email Not Valiadte")      