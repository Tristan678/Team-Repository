#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:53:17 2023

@author: ganaht1
"""

import Tristan

import #your file name

try:
    results =Tristan.read_csv_file()
except FileNotFoundError:
    print(f"Error: File '{Tristan.read_csv_file}' not found.")
else:

#your try and except



    filename = 'example.txt'
    contents = Tristan.read_csv_file(filename)
    
    if contents is not None:
        success = write_to_file(filename, contents) #whatever you called the function
        if success:
            print("Success: File written.")
        else:
            print("Error: Failed to write file.")
