# replace function in a string 

str = "hi my name is devansh jindal and i am learning python"

str.replace("old value", "new value")

#finding a sub string in a main string 

str.find("o")
#if returns -1 mean cant find that sub string

# counting function to count the repetition of a sub strinng in the main string

str.count("subString")

#***************************** List specific functions *******************************************************************

#mutable
# ordered
# slicing works as same as strings

list = [2,1,3]

list.append(4) # add one more element at last

list.sort() #sorts in ascending order

list.sort(reverse=True) # sorts in descending order

list.reverse() # reverse the list

idx = 2
el = 45
list.insert(idx, el) # inserts an element at a perticular index number

list.remove(2) # removes the first occurance of that element

list.pop(idx) # removes element at a perticular idx


#************************************** Tupples **************************************************************************

# ordered
# slicing works as same as strings

# tupples are same as lists just the difference is we canot change the item of a tupple and list is defined with [] these brackets but tupples are defined with () these brackets

tup = (1,2,3,4,5,6)

tup.index(2) # find the index of first occurance

tup.count(2) # count the number of repetition

#************************************ Dictionary *************************************************************************

# unordered
# dictionary are just like objects which stores the data in key value pairs
# we cant change the name of a key

# eg. 

dict1 = {
    "name": "devansh",
    "class": "BCA",
    "UID" : 2316002
}

print(dict1)

# dictionary can be in nested form which mean we can have a dictionary in other dict

dict1.keys() # return all the keys in the dictionary

dict1.values() # returns the value of every key a dictionary is holding

dict1.items() # returns all the key value pairs in dictionary as a tupple

dict1.get("key")  # returns the value of the key without giving an error on mismatch

dict1.update({"key" : "value"}) # update the existing dictionary by adding more key value pairs and can also overrwrite the value of any pre existing key

#**************************************** SETS ***************************************************************************

# list and dictionary are not allowed as an elements in set
# sets are mutable mean we can add or remove elements in set
# unordered
# element of a set are always unique to eacg other if the value repeats it will ignore that repetition

# eg.
set1 = {1,2,3,4,5,6,7,8,9,1}

# syntax to set an empty set is 

collect = set()

set1.add(21) # add elements in set

set1.remove(21) # removes the element in set

set1.clear() # empties the entire set

set1.pop() # removes the random value from set

set1.union(collect) # combines all the values of both the set 

# eg. for union set1 = {1,2,3} set2 = {2,3,4} it will return a new set with values {1,2,3,4}

set1.intersection(collect) # combine all the common values in both set and the differernce is ignored

# eg. for intersection set1 = {1,2,3} set2 = {2,3,4} it will return a new set with values {2,3} as 2 and 3 are common in both sets

#                             LOOPS

#********************************* While Loop ****************************************************************************

# while condition:
#     statement

#*************************** for loop ************************************************************************************

# for el in item:
#     statement
# else:
    # if you wish to do something on the end of loop

# if break is used else part will not be triggered

# for i in range(5):
#     statement


# range 

# range(start val, end before , step size mean increment)