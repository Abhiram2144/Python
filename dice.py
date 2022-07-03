import random
dice = [1,2,3,4,5,6]
while True :
    x=random.choice(dice)
    print("your dice number is :{} ".format(x))
    a=input("if u wanna roll again type Y else N :")
    if a.lower() != 'y':
        print("thanks for playing :) ")
        break
