"""
Title:   InClass_05_data_IO_part1.py
Purpose: Learn one way to read data from a file.
Author:  ** YOUR NAME HERE **
Date:    ** ENTER DATE HERE **
"""

# To complete this assignment, you must also download the
# accompanying text file called "US_state_populations.csv". It 
# contains the names of all 50 states, their 2019 estimated population,
# and their 2010 census population (from Wikipedia). Once
# you have downloaded this file, put it in the same working 
# directory (folder) as this .py file. That way, Python will know 
# where to look for the data 


# TASK:
#  Read in the data in the "US_state_populations.csv" file line-by-line
#  using a while loop. Although this is not the most convenient way to
#  read in data like this, it is an informative start to our discussions
#  of data input/output. 


# DETAILS:
#  Store the entries from the first column in a list.
#  Store the entries from the second and third column in two separate
#    NumPy arrays.
#  The entries are separated by commas ",", hence the file extension
#    CSV or  "comma-separated values"
#  The first row of the dataset is a header (it tells you what the 
#    columns contain). Do not include the header in your data. The 
#    first entry in the header row is "#". This is a typical practice
#    and usually distinguishes header information from the actual data.
import numpy as num

f=open('US_state_populations.csv','r')
#State ArrayS
states=[]
pop=[]
#Do not know what num array is for yet

#Reading lines 
line1=f.readline()

for line in f:
    x=line.split(",")
    states.append(x[0])
    pop.append(x[1:3])

#Create a 3D ARRAY to store arrays for states,pop2019,2010
USPOP=num.array([[states], [pop]])
#Sort The Arrays Least to Greatest
w=num.argsort(USPOP,2)
#Find percentages, some may have decreased
print(pop)

        



    #states.append(f.readlines())
