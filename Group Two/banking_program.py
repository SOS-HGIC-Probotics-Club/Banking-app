#create a program to add or subtract money from the main balance of a bank account

#ask user for main balance
main_balance=float(input("Enter your main balance:"))

#ask user if they want to put in or remove money
answer1=str(input("Would you like to deposit or withdraw money?"))
if answer1=="deposit":
    add=float(input("How much money would you like to deposit into your account?"))
    final_balance=main_balance+add
    print(final_balance)
elif answer1=="withdraw":
    subtract=float(input("How much money would you like to withdraw from your account?"))
    final_balance1=main_balance-subtract
    print(final_balance1)

