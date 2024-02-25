numbers = [5,4,2,1 ,7, 4 ];

# appending in a list
numbers.append(20)
print(numbers)

# inserting a number a particular index
numbers.insert(2,3)
print(numbers)

# pop
numbers.pop()
print(numbers)

# clear method removes all elements from the list
# numbers.clear()
# print(numbers)

print(numbers.count(4))

# copying a list
numbers2 = numbers.copy()
numbers.append(1)
print(numbers2)
print(numbers)

# checking the existence of element
# 1. in return boolean value , works on strings

print(50 in numbers)

# 2. index method returns index of value if present in the list

print(numbers.index(2))
print(numbers.index(1, 2 ))
print((numbers.index(7,3,6)))

# removing element from the list
numbers.remove(3)
print(numbers)

# sorting the list
# numbers.sort()
# print(numbers)


# reverse sorting the list
numbers.sort()
numbers.reverse()
print(numbers)



# program to remove duplicates from the list
uniques = []

for item in numbers:
    if item not in uniques:
        uniques.append(item)

numbers = uniques
print(numbers)