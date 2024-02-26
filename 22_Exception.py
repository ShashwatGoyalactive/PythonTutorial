# Exception can be handled in python using try except finally 
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value entered')
except:
    print('Unknown error occured')
finally:
    print('clearing the resources ')