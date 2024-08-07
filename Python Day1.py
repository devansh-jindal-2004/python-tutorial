
name = "devansh"
print(name)
print("hello")


                                # Expression excecution

# case 1 when string and numeric value is multiplied

a,b=2,3
txt="@"

print(a*txt*b)

# ANSWER = @@@@@@ //6TIMES @ AS A * B IS 6 AND 6 * STRING WILL RESULT IN 6 TIMES REPETITION OF THAT STRING 

                                # CASE 2 CONCATINATION

A,B = "2",3
txt="@"

print((A+txt)*B)

# ANSWER = 2@ 3 TIMES 

                                # CASE 3 All operators work with numeric value

a,b =2,3
c=4
print(a+b*c)

# ANSWER = 14

                                # CASE 4 multiply float with int result in float

a,b=4,5.0
c=a*b

print(c)

# ANSWER = 50.0

                                # CASE 5 division on 2 int will result in float variable

a,b = 2,2
c = a/b
print(c)

#ANSWER 1.0

                                #CASE 6 intezer division of int and float will result in int displayed as float

a,b = 1.5,3
c= a//b
print(c, a/b)

#ANWER //means intezer division in python which mean it will removes decimal value C = 0, a/b= 0.5

                                #CASE 7 remainder is negative when denominator is negative

a,b = 5,-2
c=a%b
print(c)

#ANSWER -1

# ************************************************************************************************************************


    #INPUT FUNCTIONS

#input of a string
name = input("Name : ")
print(name)

#input of a int

age = int(input("Age : "))
print(age)

#input for float

price = float(input("price : "))
print(price)

#*************************************************************************************************************************

    #CONDITIONAL STATEMENTS 

"""if(condition1):
#     statement 1
# elif(condition2):    elif mean else if in c language
#     statement 2
# else :
#     final statement"""


# single line if statement

    # statement if (condition) else final statement

# clever if (not commonly used)

    # (false statement, true statement) [condition]