#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:39:50 2023

@author: ganaht1
"""





import csv

def read_csv_file(filename):

    with open(filename, 'r') as csvfile:
       
        reader = csv.reader(csvfile)

        output = []

        for row in reader:
            if len(row) > 0:
                output.append(row)

        return output


