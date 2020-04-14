"""
Shirley Wu
ICS3U
Date: 03/07/2019
Practical test
"""

#print welcome message
print("WELCOME to ICS Bank!")

pin = "190307"
Checking = 253
Saving = 6250

user = input("Please enter your PIN: ") #Ask for pin
attemps = 2

while user != pin and attemps > 0: 
    print("Wrong PIN. %d attemps remaining." %attemps) #Ask for pin again
    attemps -= 1
    user = input("Please enter your PIN again: ")
if attemps < 0:
    print("Tries exceeded. Account is now locked.")

#allow access to account
if user == pin:
    print("Now you have access to your account.\n")
    
def start_banking(c,s):
    selections = ["Make a selection:", "1. View Balance","2. Make a Withdrawal","3. Make a Deposite","4. Transfer Money", "0 to Exit."]
    for i in selections:
        print(i)
    selection = int(input(">>> "))

#define each actions

    def end (c,s):
        the_end = ("\nThanks for banking!\n\n-------- Receipt --------\nChecking Account: $ %.2f \nSaving Account : $ %.2f" %(c, s))
        print(the_end)
        return ("")
    
    def view_balance (c,s):
        account = input("\nFrom Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            a =("Checking Account : $ %.2f" %c)
            print(a)
            return (continue_banking(c,s))
        elif account == '2':
            b =("Saving Account: $ %.2f" %s)
            print(b)
            return (continue_banking(c,s))
    
    def withdrawal (c,s):
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to withdraw: "))
            c -= amount
            print("Checking account balance: $%.2f"%c)
            return (continue_banking(c,s))
        elif account == '2':
            amount = float(input("Enter an amount to withdraw: "))
            ask = input("$4 fee for withdrawing from Savings. Continue? Y/N >>> ")
            if ask  == "Y":
                s -= (amount+4)
                print("Saving account balance: $%.2f"%s)
                return (continue_banking(c,s))
            else:
                return (continue_banking(c,s))
            
    def continue_banking (c,s):
        continue_b = input("\nContinue Banking? Y/N >>>")
        if continue_b == 'Y':
            return (start_banking(c,s))
        else:
            return (end(c,s))

    def deposit(c,s):
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to deposite: "))
            c += amount
            print("Checking account balance: $%.2f"%c)
            return (continue_banking(c,s))
        elif account == '2':
            amount = float(input("Enter an amount to deposite: "))
            s +=amount
            print("Saving account balance: $%.2f"%s)
            return (continue_banking(c,s))

    def transfer(c,s):
        account = input("From Account: \n1. Checking\n2. Savings\n>>> ")
        if account == '1':
            amount = float(input("Enter an amount to transfer: "))
            c -= amount
            s += amount
            print("Checking account balance: $%.2f \nSaving account balance: $%.2f" %(c,s))
            return (continue_banking(c,s))
        elif account == '2':
            amount = float(input("Enter an amount to transfer: "))
            c += amount
            s -= amount
            print("Checking account balance: $%.2f \nSaving account balance: $%.2f" %(c,s))
            return (continue_banking(c,s))
            

#return results
    if selection == 1:
        print(view_balance(c,s))
    elif selection == 2:
        print(withdrawal(c,s))
    elif selection == 3:
        print(deposit(c,s))
    elif selection == 4:
        print(transfer(c,s))
    elif selection == 0:
        print(end(c,s))
    else:
        print("INVALID INPUT")
    return ("")

#begin program
print(start_banking(Checking, Saving))
