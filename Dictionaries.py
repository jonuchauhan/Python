"""dictionary represent the element arranged in a key value pair
"""

# creating a dictionary

a = {}

# in dictionary elements are separated by comma and key value  pairs are separated by single colon

a = {"name": "jonu chauhan", "dept": "IT", "Salary": 2000}

print(a["name"])
print(a["dept"])
print(a["Salary"])

# iterating in dictionary

for key, values in a.items():
    print(key, '-', values)

# iterating the keys of dictionary

for keys in a.keys():
    print(keys)

# iterating values in dictionary

for values in a.values():
    print(values)

# adding key and value pair to dictionary

a["city"] = "Helsinki"

print(a)
# updating the dictionary

a["city"] = "oslo"

print(a)

# dictionary comparision

names = ['jonu', 'varun', 'karan']
marks = [10, 20, 30]

result = {k: v for (k, v) in zip(names, marks)}
print(result)


# another way by creating a function to combine list into a dictionary
def zip_dic(a, b):
    """passing two list as parameter and and creating a new dictionary with zip function"""
    c = zip(a, b)
    d = {}
    for k, v in c:
        d[k] = v
    return d


result = zip_dic(names, marks)
print(result)

import operator

# sorting the list

# sorting by keys
marks = {'jonu': 60, 'varun': 20, 'karan': 900}

a = sorted(marks.items())

# sorting by keys
"""sorting on the basis of values can be done by using the key paramter 
with operator.itemgetter(1)"""

a = sorted(marks.items(), key=operator.itemgetter(1))
print(a)

# clear statement is used to clear the dictionary

marks.clear()
print(marks)
