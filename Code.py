import time
import random
start=time.time()
temp=random.randint(0,100)
print("Welcome to the first project attempt of a rookie programmer!")
time.sleep(2)
print("Can ya guess What it IS !?")
time.sleep(2)
print("Can ya     G_U_E_S_S        what it IS!?")
time.sleep(3)
print("Its a number guessing game, you idiot!")
time.sleep(2)
print(" (-_-)")
time.sleep(1)
while True:
    try:
        n=input("Enter your guess! (Integers Please)")
        n=int(n)
        if n==temp:
            print("Congrats!")
            time.sleep(1)
            print("Congratulations on wasting %s seconds of your life!" % (time.time() - start))
            time.sleep(1)
            print("...")
            time.sleep(2)
            print("Idiot..")
            print("Bubbye!")
            quit()
        elif n>temp:
            print("Thoda neeche!")
        elif n<temp:
            print("Thoda upar!")

    except ValueError:
        time.sleep(1)
        print("('-_-)")
        time.sleep(2)
        print("AN INTEGER YOU IDIOT")
