# your name is : S ABHIRAM
# your card number is : 4433-5577-1133
#your card's expiry date is : 12/27
#your cards CVV is : 143
#your card's pin is : 2144
#your account has this much money already : 50,000
amount = 50000
class Bank:
       def start(self):
              print("Please insert your card below : ")
              print(50 * "_")
              a = input("if inserted press Y to check :   ").lower()
              if a != 'y':
                     print("please insert your card ")
                     a= input("if inserted press Y to check").lower()

              print(50*" ")
              print(50*"_")
              num = int(input("For our security purposes please enter your card number below  :"))
              i,k=0,0
              if num != 443355771133:
                  while i<2:
                     print("enter the correct number sir : TRY AGAIN ")
                     num = int(input("For our security purposes please enter your card number below  :"))
                     i = i + 1
                     if num == 443355771133:
                              break

                  print("sorry your card number was wrong for too many times! \n Please try tomorrow :)")
                  exit()
              pin=int(input("Now please Enter your Pin number of your card : \n \n "))
              if pin != 2144:
                     while k < 1:
                            pin = int(input("Now please Enter your Pin number of your card carefully, Its your last chance  :\n \n "))
                            k=k+1
                            if pin != 2144: exit()
       def deposite(self):
              print("By choosing this option you are going to deposite the required money now. ")
              print("your money remaining in the account is "+str(amount))
              print(50 * "_")
              add = int(input("Enter the amount of money you are going to depoiste : "))
              ask = input("Are you sure!! Do you want to deposite this amount in your bank account \n Press Y if YES : ").lower()
              if ask =='y':
                     print("Request pending...")
                     print(50 * " ")
                     print("*SUCCESS, Your money has been deposited to your account!!!*")
                     print("Total money in your account now is {}".format(add+amount))
                     print("Thanks for your approach, Visit Again :) \n \n ")
                     exit()
              else :
                     print("OHHH! Better start from the begining Sir ! \n GOOD LUCK :) \n \n ")
                     exit()
       def withdraw(self):
              print("By choosing this option you are going to withdraw the required money now. ")
              print("your money remaining in the account is "+str(amount))
              print(50 * "_")
              add = int(input("Enter the amount of money you are going to withdraw  : "))
              ask = input("Are you sure!! Do you want to withdraw {} in your bank account \n Press Y if YES : ".format(add)).lower()
              if ask =='y':
                     print("Request pending...")
                     print(50 * " ")
                     print("*SUCCESS,Take your money from below *")
                     print("Total money in your account now is {}".format(amount - add))
                     print("Thanks for your approach, Visit Again :) \n \n ")
                     exit()
              else :
                     print("OHHH! Better start from the begining Sir ! \n GOOD LUCK :) \n \n")
                     exit()
       def checkdetails(self):
              print("By choosing this option you will be checking your account details : \n \n ")
              print(" Your name is : S ABHIRAM \n \n  Your card number is : 4433-5577-1133 \n \n Your card's expiry date is : 12/27 \n\n Your cards CVV is : 123 \n \n Your card's pin is : 2144 \n\n Your account has this much money already : 50,000")
              print("Thanks for your approach, Visit Again :) \n \n ")


bank=Bank()
bank.start()
print("Now you have to decide what you want to do : ")
print("The available options are : \n 1) Deposit \n 2) Withdraw \n 3) Check account details.   ")
choice = int(input("\n You have to press the number according to the option given :"))
if choice == 1 :
       bank.deposite()
elif choice == 2 :
       bank.withdraw()
elif choice == 3 :
       bank.checkdetails()
else :
       print("You entered a invalid number. Try from starting again!! ")
       exit()