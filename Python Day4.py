#*********************** Functions ***************************************************************************************

# def keyword is used to define a function in python language

# eg.
def sum(a,b):
    return a+b

print(sum(5,10))

#********************** File handeling ***********************************************************************************

# open file

f = open("demo.txt", "+a")  # mode : read (r) or overwrite (w) or create and write (x) or add data to existing file (a) 

# (b) to open file in binary mode

# read file

data = f.read()

print(data)

# overwrite file

f.write("\nthis in new data")

data = f.read()

print(data)

# close file

f.close()


# with syntax

with open("demo.txt", "r") as f:
    data = f.read()


# deleting file

import os

os.remove("demo.txt")