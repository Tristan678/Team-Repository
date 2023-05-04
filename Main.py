#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:53:17 2023

@author: ganaht1
"""

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def write_to_file(filename, contents):
    try:
        with open(filename, 'w') as file:
            file.write(contents)
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

filename = 'example.txt'
contents = read_from_file(filename)

if contents is not None:
    success = write_to_file(filename, contents)
    if success:
        print("Success: File written.")
    else:
        print("Error: Failed to write file.")
