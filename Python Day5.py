#******************************* OOP (object oriented programing) ********************************************************

# defining a class

class student:

    Name = "devansh" # class atributes

    #default constructors
    def __init__(self):
        
        print("default constructor")

    # parameterized consttructors
    def __init__(self, parameter): # passing self as perimeter is mandatory
        self.parameter = parameter #object atributes   
        # to make anything private just add __ ( 2 underscores )

    # private variables are those which can only be acessed inside class defination and cant be acessed outside of that

    # defining static methodes
    @staticmethod # static method are used where we dont need to access the object
    def hello(): 
        print("hello")



s1 = student("parameter")
print(s1.parameter)

# del key used to delete an object key or an object

del s1

# print(s1)


class student1(student): # intereted student class to student1
    rollno = "808080"

st= student1("para")
print(st.Name, st.rollno)


# super().__init__ used to call any method of parent class