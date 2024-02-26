class Mamal:
    def walk(self):
        print('walk')


class Dog(Mamal):
    def bark(self):
        print('bark')



class Cat(Mamal):
    def meow(self):
        print('meow')



dog1 = Dog()
dog1.bark()
dog1.walk()


cat1 = Cat()
cat1.walk()
cat1.meow()
