course = 'Python for Beginners'

''' difference between method and function
 methods are specific to classes like string and function are not specific to a class or object '''


# len is a method
print(len(course))

print(course.upper())
print(course)
print(course.lower())

''' difference between "find" and "in" operator  
    "find" operator returns the index of the first matching character or sequence of characters 
    where as "in" method returns the boolean value
'''


print(course.find("B"))
print(course.find('Beginners'))

print(("for" in course))
# the next executing statement will return false because python is case-sensitive language
print("For" in course)
print('f' in course)


# replacing a character or sequence of characters from the existing string

print(course)
# modifying the original variable content
# course = course.replace("Beginners" , "Absolute Beginners")

# making temporary changes which do not modify the original string
print(course.replace("Beginners" , "Absolute Beginners"))

print(course)