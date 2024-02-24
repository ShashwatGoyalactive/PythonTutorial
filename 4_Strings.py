# course = "Python's course for Beginners "
# print(course)
#
# course = 'Python for "Beginners"'
# print(course)
#
# course = '''
#
# Hi John,
#
# This is our first letter to you
# Thank You
#
# Team Support
#
# '''
#
# print(course)


course = 'Python for beginners'

# Acessing value at indexes in String

print(course[0])
print(course[1])
print(course[2])
# python has a feature of accessing indexes from last called as negative index
print(course[-1])
print(course[-2])


# a range of elements can also be accessed in python

print(course[0:4])
print(course[:4])
print(course[1:-1])
print(course[4:])

# copying a part of string to another variable

another = course[3:-2]
print(another)