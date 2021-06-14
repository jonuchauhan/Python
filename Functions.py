# Functions are block of code that are intended to do perform some task.

# defining a function
def hello_world():  # functions are defined with def keyword followed by a name (in lower case) and parenthesis

    print("Hello World")


hello_world()  # calling a functions


# passing a parameter to a function
def say_hi(name):
    print("Hello {}".format(name))


say_hi("jonu chauhan")


# passing fixed number of multiple values to a functions with return statement

def sum_of_values(a, b):
    return a + b


result = sum_of_values(10, 12)
print(result)


# returning multiple values

def calc(a, b):
    sum_of_val = a + b
    diff_of_val = a - b
    mul_of_val = a * b
    div_of_val = a / b
    return sum_of_val, div_of_val, mul_of_val, diff_of_val


result = calc(10, 12)
print(result)  # this function will return list of value in tuple


# default arguments

def salary_hike(name, salary, hike=.5):
    hiked_salary = salary + (salary * hike)
    print("old Salary for {} is {} and New Salary is {}".format(name, salary, hiked_salary))


salary_hike("Jonu", 100000)

# variable length arguments

"""There are two types of variable length arguments
    first one is args and  secondly kwargs,variable length arguments are starts with 
    '*' like *args and *kwargs"""


# args

# sum functions with multiple values


def sum_of_values(*args):
    """*args takes the elements and stores them in tuple"""
    sum = 0
    for val in args:
        sum = sum + val
    return sum


a = sum_of_values(1, 2, 3, 4, 5, 6, 7, 8, 10, 1, 9898, 101010)

print(a)


def employee_details(**kwargs):
    for key, value in kwargs.items():
        print("Key {} and its Value is {}".format(key, value))


employee_details(name="jonu", sal=10000, dept="IT")

# Global and Local variable

"""Local variable is a variable whose scope is limited to a particular function
    and on other hand global variable scope is available to entire program"""

a = 1  # a is global variable


def modify():
    a = 2  # here a is local variable  and its scope is limited to only this function
    print(a)


modify()
print(a)

"""if we need to use global variable in a function we can assign 
    the value of global variable to a function variable and use it with function called global()"""

"""global() is a built in function which provides the list of global variables in a form of 
dictionary"""
hike = 9


def use_global_variable(salary, dept):
    if dept == "IT":
        temp_hike: int = globals()['hike'] + 2
        salary = salary + salary * temp_hike * .01
    else:
        salary = salary + salary * hike * .01

    return salary


a = use_global_variable(10000, "IT")
print(a)
a = use_global_variable(10000, "HR")
print(a)

# function decorators

"""decorators accepts function as paramter and return function as a result"""


def decor(func):
    def inner():
        val = func()
        modify_val = val + 1
        return modify_val

    return inner


@decor  # this statement tells that a decorator is applied on a below function
def num():
    return 10


print(num())

"""special variable named ___name__"""

"""this tells weather program is executed as an individual program or as an module"""


def display():
    print("hello world")


if __name__ == '__main__':
    display()
    print("this is executed as a program")
else:
    print("this is executed as a module")


