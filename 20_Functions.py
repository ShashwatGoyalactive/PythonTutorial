# funcion can be defined in python using def keyword

# non parameterized constructor
def greet_user():
    print("Hi there!")
    print("Welcome Abode")


# parameterized function
def greet_user1(name):
    print(f'Hi {name}')
    print('welcome abode')


# print("Start")
# greet_user()
# greet_user1('Shashwat')
# print("Finished")


# keyword agument vs parameterized argument

''' parameterized arguments are passed in the order in which they 
    defined in the function definition ie the position of argument really matters 
    in the case of parameterized arguments 
    
    keyword arguments imporves readability of code by passing name along with the argument 
    in the function call 
    
    Note:- It is important to note that the keyword arguments are always follow parameterized agument i.e either 
    all the function call arguments are keyword argument or the non keyword (oarameterized) arguments are passed 
    before the keyword arguments
  
'''


def func_call(first_name , last_name):
    print(f'Welcome {first_name} {last_name}')


#     parameterized call
func_call("John" ,"Smith")
func_call("Bill" , last_name="Clinton")
func_call(last_name="Page" , first_name="Larry")
func_call(first_name="Bill" , last_name="Gates")
