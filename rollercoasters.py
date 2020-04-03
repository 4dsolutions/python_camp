# -*- coding: utf-8 -*-
"""
Created on Tues Feb 14, 2017

@author: kurner

Reads a csv file and prepares data for insertion into SQL Lite.

Running this top level proves the file is being read
(or not).  The data is not saved anywhere, once read.

http://stackoverflow.com/questions/603572/how-to-properly-escape-a-single-quote-for-a-sqlite-database

"""

import csv
from collections import namedtuple

Coaster = namedtuple("Coaster", ['Name', 'Park', 'State', 
                                 'Country', 'Duration', 'Speed', 
                                 'Height', 'Drop', 'Length', 
                                 'Yr_Opened', 'Inversions'])

def read_csv(console=False):

    all_coasters = {}    # initialize main dict
    
    with open('./data/roller_coasters.csv', newline='') as csvfile:
        roller_reader = csv.reader(csvfile)  # use the included reader
        header=True
        for row in roller_reader: # skip first line
            if header:
                header=False
                continue
            
            # see linked stackoverflow question for why ' is replaced with ''
            row = [s.replace("'","''") for s in row]  # sqlite needs
            coaster = Coaster(*row)  # named tuple
            all_coasters[coaster.Name] = coaster      # main dict
            if console:
                print("{:25} | {:26} | {:15} | {:5}".
                        format(row[0][:25], row[1][:26], row[2][:15], row[3][:5]))

    return all_coasters
    
if __name__ == "__main__":
     # this won't run when the module is imported
     the_data = read_csv(console=True)  # echo to console
     
