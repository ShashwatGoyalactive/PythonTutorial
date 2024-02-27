import random
for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))


members = ['John' , 'Mosh' , 'Harry' , 'Bill']

leader = random.choice(members);
print(leader)

# roll a pair of dice

from Dice import dice
print(dice)