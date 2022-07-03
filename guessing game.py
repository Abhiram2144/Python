import random
comp = random.randint(1,10)
def game():
    player = 0
    while player != comp:
        player = int(input("enter your number here : "))
        if player > comp :
            print(" yooo  too high!!!")
        elif player < comp:
            print("too low!!")
game()
print("yes you get it :)")
a = input("if u wanna play again type y or else n :")
while a != 'n':
       game()
       print("yes you get it :)")
if a == 'n':
    exit()

