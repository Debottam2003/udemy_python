from functools import reduce

# Exceptions
# ZeroDivisionError	Raised when dividing by zero.
# ValueError	Raised when a function gets a valid type but invalid value.
# TypeError	Raised when an operation is applied to an object of an inappropriate type.
# NameError	Raised when a variable is not defined.
# IndexError	Raised when accessing a list index out of range.
# KeyError	Raised when accessing a non-existent dictionary key.
# FileNotFoundError	Raised when trying to open a file that doesn’t exist.
# ImportError	Raised when an import statement fails.
# AttributeError	Raised when an invalid attribute reference is made.

arr = [7,8,9,2,3,5,10,13,21]
# syntax map(function, iterable)
def square(x):
    return x*x
squared_arr = list(map(square, arr))
print(squared_arr)
print(arr)

# syntax filter(function, iterable)
def filter_even(x):
    return x%2==0
even_arr = list(filter(filter_even, arr))
print(even_arr)

# syntax reduce(function, iterable)
def add(x,y):
    return x+y
sum_arr = reduce(add, arr)
print(sum_arr)