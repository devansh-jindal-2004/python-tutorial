# ************************************** Types of methods ****************************************************************

# @static methods (dont take any default argument)
# @class methods (takes class as first argument)
# @instance methods  (takes self as first argument)


# @property  this decorator is used when value for one variable/atribute depends on other so when using this whenever the value of any atribute changes it will run itself

# syntax:

# class student :
#     @property
#     def name_for_atribute(self):
#         return Logic_to_calculate_value


# ************************************ operators & dunder functions ******************************************************

# these are used to define your own logic for any airthematical operation on user defined classes 
# these are defined within the class 
# for example __add__ is a funcction which can be used to define your own logic for + operation