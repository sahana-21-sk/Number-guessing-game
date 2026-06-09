import random
num=random.randint(1,100)
while(True):
    n1=int(input("Guess the number between 1 and 100: "))
    if(n1>num):
        print("Too high!")
    elif(n1<num):
        print("Too low!")
    else:
        print("congratulations! you guessed the number!!")
    if(type(n1)!=type(10)):
        print("Enter a valid number!")
    if(n1==num):
        break