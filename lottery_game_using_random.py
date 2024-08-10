import random

play = input("Write play to start and quit to quit the game: ")
number

while(play!="quit"):
    print("Hello Welcome to our lottery show")
    name=input("Enter Yur name: ")
    lotterynumber=random.randint(1,5)
    guess=int(input("Enter a number: "))
    if lotterynumber==guess:
        print(f"Hurrah! {name} you have one a Lottery worth $5M. Lottery Number is:",lotterynumber)
    else:
        print(f"{name}: Good luck for next time",lotterynumber)
    play=input("Write play to start and quit to quit the game: ")


