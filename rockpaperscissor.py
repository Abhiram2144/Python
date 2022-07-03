import random
while True :

   choices = ['rock','paper','scissors']
   player = None
   x=random.choice(choices)
   while player not in choices:
      player = input("rock,paper,scissors : ").lower()
   print("your choice  is "+player," and computer choice is "+x)
   if x == player :
      print("tied!")
   elif player=="rock":
       if x=="paper":
            print("you lose")
       if x == "scissors":
            print("you win")
   elif player=="paper":
       if x=="rock":
            print("you win")
       if x == "scissors":
            print("you lose")
   elif player == "scissors" :
       if x == "paper":
            print("you win")
       if x == "rock":
            print("you lose")

   play_again=input("if you want to play type Y/N")
   if play_again!='Y':
       break