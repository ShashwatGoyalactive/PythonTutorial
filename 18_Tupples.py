# we can only get information about tupple we cannot modify it
numbers = (1,2,3)
print(numbers)
# numbers[0] = 2 uncommeting this code will generate error
# print(numbers)

coordinates = (1,2,3)
# x= coordinates[0]
# y=coordinates[1]
# z=coordinates[2]

# alternative to the above code (unnpacking)

x,y,z = coordinates
print(f'{x} , {y} , {z}')