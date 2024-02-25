import math
names = ['John' ,'Bob' , 'Mary' , 'Sarah' , 'Mosh' , 'James' ]
print(names[1:5])
print(names[-1])

numbers = [1 ,6,12,-1 , 4,2,0]

max = numbers[0]

for i in numbers:
    if(max < i):
        max = i

print(max)