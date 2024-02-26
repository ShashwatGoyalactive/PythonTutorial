class Point:

    def __init__(self , x ,y):
        self.x = x;
        self.y = y;
    def move(self):
        print("move")

    def draw(self):
         print("draw")


# object
# point1 = Point()
# point1.x = 10
# point1.draw()
# point1.move()
# print(point1.x)

point = Point(10,20)

'''
   1. Every method inside a class must have 'self' as its first parameter
   2.'self' can be used to access the current object variables 
    3. __init__(self) is a constructor 
    
    '''

class Person:
    def __init__(self , name ):
        self.name = name

    def introduce(self):
        print(f'Hi I am {self.name}')



person1 = Person("Shashwat")
person1.introduce()
