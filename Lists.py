"""List is like an array that contains a group of element in specific order"""

a = []  # creation of a list

a = [1, 2, 3, 4, 5, 6, "jonu chauhan"]
print(a)

# generating List with range function
a = list(range(0, 10, 1))
print(a)

# iterating through the list

for values in a:
    print(values)

# itterating through the index of list

i = 0
while i <= len(a) - 1:
    print("item no {} in list is {}".format(i, a[i]))
    i += 1
# adding element to the list

"""append is a function to add element to the list"""
print(a)
a.append(100)
a.append(101)
a.append(102)

print(a)

# updating the value of list

a[10] = 99
print(a)

# removing the element from the list

a.remove(99)
print(a)

# slicing into the list


# key to remember here is  start:stop:step
# in below example start is 0 and stop is 5
print(a[0:5])  # start is 0th position and 5th is the last position

print(a[4:5])  # start position is 4th index and 5th is the end and step is none

"""in list index start from 0 and from end it start from -1"""

print(a[-6:-1])

# taking every nth element of the list

print(a[::2])

new_list = a

print(new_list)

new_list[:4] = [99, 98, 97, 96]  # updated the first four values of list with the given parameters
print(new_list)

new_list[5:8] = [-1, -2, -3]

# finding common element within list
print(a)
new_list = [100, 101]
print(new_list)

common_element = list(set(a).intersection(set(new_list)))
print(common_element)


def common_element_in_list(a, b):
    a = set(a)
    b = set(b)

    return list(a.intersection(b))


common_element = common_element_in_list(a, new_list)
print(common_element)

# Nested List

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0])  # list at 0th index

# accessing the nested list elements


print(nested_list[0][0])  # first index is for first nested list and second one is for index of element within first
# list
