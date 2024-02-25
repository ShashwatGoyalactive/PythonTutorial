i =1
while i<= 5:
    print(i)
    i=i+1
print('Done')

# Car game that understands only three commands : (start , stop , quit )

print("Choose the operations to operate the car..")
print("start: Car started... Ready to go!")
print("stop: Car stopped .")
print("quit: exit the game")

cmd = input('Enter your choice : ')

while cmd.upper() !="QUIT":
    cmd = input('Enter your choice : ')
    if cmd.upper() == 'START':
      print("Car started... Ready to go!")
    elif cmd.upper() == 'STOP':
        print("Car stopped .")
    elif cmd.upper() == 'QUIT':
     print("exit the game ")
    else :
        print("Command not recognized")

