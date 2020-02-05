"""
Shirley Wu
ICS3U
Date: 03/07/2019
Practical test
"""

#print welcome message
print("WELCOME to ICS Bank!")

pin = "190307"

user = input("Please enter your PIN: ") #Ask for pin
attemps = 2

while user != pin and attemps > 0: 
    attemps -= 1
    print("Wrong PIN. %d attemps remaining." %attemps) #Ask for pin again
    user = input("Please enter your PIN again: ")
if attemps == 0:
    print("Tries exceeded. Account is now locked.")

#allow access to account
if user == pin:
    print("Now you have access to your account.")
    selections = ["Make a selection:", "1. View Balance","2. Make a Withdrawal","3. Make a Deposite","4. Transfer Money", "0 to Exit."]
    for i in selections:
        print(i)
    selection = int(input(">>> "))

#define each actions
    a = 253
    b = 6250

    def end (x,y):
        the_end = "\nThanks for banking!\nReceipt:\n-------------------\nChecking Account: $" + str(x) + "\nSaving Account : $" + str(y)
        return the_end
    
    def view_balance ():
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            a =("Checking Account : $253")
            return a
        elif account == '2':
            b =("Saving Account: $6250")
            return b
        return end
    
    def withdrawal ():
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to withdraw: "))
            c_money = a - amount
            s_money = b
            return("Checking account balance: $%.2f"%c_money)
        elif account == '2':
            amount = float(input("Enter an amount to withdraw: "))
            s_money = b - amount
            c_money = a
            ask = input("$4 fee for withdrawing from Savings. Continue? Y/N >>> ")
            if ask  == "Y":
                return("Saving account balance: $%.2f"%s_money)
            
        continue_banking = input("Continue Banking? Y/N >>>")
        if continue_banking == 'Y':
            for i in selections:
                print(i)
            selection = int(input(">>> "))
        else:
            return(end(c_money,s_money))
            

    def deposit():
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to deposite: "))
            c_money = a + amount
            s_money = b
            return("Checking account balance: $%.2f"%c_money)
        elif account == '2':
            amount = float(input("Enter an amount to deposite: "))
            s_money = b + amount
            c_money = a
            return("Saving account balance: $%.2f"%s_money)
        continue_banking = input("Continue Banking? Y/N >>>")
        if continue_banking == 'Y':
            for i in selections:
                print(i)
            selection = int(input(">>> "))
        else:
            return(end(c_money,s_money))
            

    def transfer():
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to transfer: "))
            c_money = a - amount
            s_money = a + amount
            return("Checking account balance: $%.2f"%c_money)
            return("Saving account balance: $%.2f"%s_money)
        elif account == '2':
            amount = float(input("Enter an amount to transfer: "))
            c_money = a + amount
            s_money = a - amount
            return("Checking account balance: $%.2f"%c_money)
            return("Saving account balance: $%.2f"%s_money)
        continue_banking = input("Continue Banking? Y/N >>>")
        if continue_banking == 'Y':
            for i in selections:
                print(i)
            selection = int(input(">>> "))
        else:
            return(end(c_money,s_money))
            

#return results
    if selection == 1:
        print(view_balance())
    elif selection == 2:
        print(withdrawal())
    elif selection == 3:
        print(deposit())
    elif selection == 4:
        print(transfer())
    
