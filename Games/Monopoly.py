'''
PYTHON Monopoly
2019,05,15 -- 2019,06,06
Shirley Wu

A game of human vs AI Monopoly
With simple, shorten rules.

*House of the same color will not change anything, just to keep the game simple. No doubling the rent or anything.
'''

import random #to generate random values for dice and make decisions for AIs.

import time #outputs slowly

'''
Feedback from Dave:
- In general, variable names start with lowercase and constant names are all uppercase
- The Xjail variables should just be booleans (True or False) instead of arrays
- Replace array variables with classes
'''

#Lists to store values

#Player backpacks:current dice value, money, current position, number of "get out of jail card", previous position
player_A = [0,1000,0,0,0]
player_B = [0,1000,0,0,0]
player_C = [0,1000,0,0,0]
player_D = [0,1000,0,0,0]

#positions according to the indexs of each lists
#name of each block on the map
positions = ["GO","Red House on Albert Street","Red House on West Street", "JAIL", "Yellow House on Park Ave", "Yellow House on Church Street", "Train Station", "Pink House on John Street","Pink House on Main Street","Pink House on Evergreen Road","Chance Station","Tax Bureau", "Blue House on University Ave", "Blue House on Ocean Street"]
#current value of each house
house_value = [0,50,80,50,120,140,200,180,195,210,0,0,280,310]
#house upgrade
just_bought = ['x',0,0,'x',0,0,'x',0,0,0,'x','x',0,0] #if the house is just bought in the current round
upgrade = ['x',0,0,'x',0,0,'x',0,0,0,'x','x',0,0]#the number of times the houses are upgraded. Will be shown on the map
#Store houses each player owns
PA_house = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PB_house = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PC_house = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PD_house = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
owner = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']

#store if the player is currently in jail
Ajail = []
Bjail = []
Cjail = []
Djail = []

#a function to ouputs the map, values keeps updating and pluged in.
def printMap():
    Map =( """
|/////////////////////|/////////////////////|/////////////////////|/////////////////////|/////////////////////|
|                     |                     |                     |                     |                     |
|                     |          %s         |         %s          |         %s          |         %s          |
|                     |     Yellow House    |    Yellow House     |                     |     Pink House      |
|        JAIL         |       Park Ave      |    Church Street    |     Train Station   |     John Street     |
|                     |        $ %d        |       $ %d         |        $ %d        |        $ %d        |
|                     |          L %s        |         L %s         |                     |         L %s         |
|                     |                     |                     |                     |                     |
|/////////////////////|/////////////////////|/////////////////////|/////////////////////|/////////////////////|
|                     |                                                                 |                     |
|         %s          |                                                                 |          %s         |
|      Red House      |                                                                 |      Pink House     |
|     West Street     |                 ___         ___   ___   ___                     |      Main Street    |
|       $ %d          |         |\  /| |   | |\  | |   | |   | |   | |    \ /           |        $ %d        |
|         L %s         |         | \/ | |   | | \ | |   | |___| |   | |     /            |          L %s        |
|                     |         |    | |___| |  \| |___| |     |___| |___ /             |                     |
|/////////////////////|                                                                 |/////////////////////|
|                     |                                                              |                     |
|         %s          |          ..........................................             |          %s         |
|      Red House      |                                                                 |      Pink House     |
|    Albert Street    |                                                                 |    Evergreen Road   |
|       $ %d          |                                                                 |        $ %d        |
|         L %s         |                                                                 |          L %s        |
|                     |                                                                 |                     |
|/////////////////////|/////////////////////|/////////////////////|/////////////////////|/////////////////////|
|                     |                     |                     |                     |                     |
|                     |          %s         |         %s          |                     |                     |
|          ↑          |      Blue House     |     Blue House      |     Pay $100 Tax    |     Chance Card     |
|         G O         |     Ocean Street    |    University Ave   |                     |                     |
|                     |        $ %d        |        $ %d        |                     |                     |
|                     |          L %s        |         L %s         |                     |                     |
|                     |                     |                     |                     |                     |
|/////////////////////|/////////////////////|/////////////////////|/////////////////////|/////////////////////|
"""%(owner[4],owner[5],owner[6],owner[7],house_value[4],house_value[5],house_value[6],house_value[7],upgrade[4],upgrade[5],upgrade[7],
     owner[2],owner[8],house_value[2],house_value[8],upgrade[2],upgrade[8],
     owner[1],owner[9],house_value[1],house_value[9],upgrade[1],upgrade[9],
     owner[13],owner[12],house_value[13],house_value[12],upgrade[13],upgrade[9]))
    print(Map)


#function for the dice, p for player_p list and n for their name that will beprinted to the screen
def dice(p,n):
    num = random.randint(1,6) #roll dice by generating a random value from 1 to 6
    p[0] = num
    p[2] += num
    p[4] = p[2]-num
    
    if p == player_A:
        time.sleep(1)
        if p[4]%14 == 3 and len(Ajail)%2 !=0: #if in jail the player cannot roll this round
            p[2] = 3
            print("\nYou cannot roll the dice until next round.")
            Ajail.append(1)

        else: #Asks the player to roll the dice or view the map
            if input("\nType any letter/number or press Enter to roll.Or type 'MAP' to see the map.\n>>> ")  == "MAP":
                printMap()
                input("\nType any letter/number or press Enter to roll.\n>>> ")
                print("\nYou rolled a %d"%num)
            else:
                print("\nYou rolled a %d"%num)

            #if the player land in jail
            if p[2]%14 == 3 and p[4]%14 != 3:
                move("JAIL",p,n) #call the movement function
                Ajail.append(1)

                    
    elif p[2]%14 == 3 and p[4]%14 != 3: # for the player B,C,D (or the computer AIs) 
        time.sleep(1)
        print("\n%s rolled a %d."%(n,num)) #the computer prints out the random value generated above as their dice value
        move("JAIL",p,n)
        if p == player_B:
            Bjail.append(1)
        elif p == player_C:
            Cjail.append(1)
        elif p == player_D:
            Djail.append(1)
    elif p[4]%14 == 3:#stops the player from rolling the dice until next round
        if len(Bjail)%2 !=0:
            p[2] = 3
            Bjail.append(1)
            print("\n%s cannot roll the dice until next round."%n)
        elif len(Cjail)%2 !=0:
            p[2] = 3
            Cjail.append(1)
            print("\n%s cannot roll the dice until next round."%n)
        elif len(Djail)%2 !=0:
            p[2] = 3
            Djail.append(1)
            print("\n%s cannot roll the dice until next round."%n)

        else:
            time.sleep(1)
            print("\n%s rolled a %d."%(n,num))
    else:
        time.sleep(1)
        print("\n%s rolled a %d."%(n,num))

#a function for the chance station, variables p & n same as above
def chance_card(p,n):
    card = random.randint(1,10) #pick a random card (picking a random value from 1 to 10)
    
    if card == 1:
        if n == "You": #output results for player
            print("You've received $50 for winning the Battle Ship contest!")
            print("You now have $%d in you bank.\n"%player_A[1])
        else:
            print("%s recieved $50 for winning the Battle Ship contest\n"%n) #tell player what the AI got
        p[1]+=50 #add money to the player's backpack list
        
    elif card == 2:
        if p == "You":
            print("Here's a 'GET OUT OF CARD FREE' card, this card may be kept until needed.")
        else:
            print("%s recieved a 'GET OUT OF JAIL FREE' card."%n)
        p[3]+=1 #player's list for the number of cards increase by one
        
    elif card == 3:
            move("JAIL",p,n) #move the player into jail
            p[2] = 3 #change the position
    elif card == 4:
        move("CC4",p,n) #call the movement functions to change player's positions, same as below
    elif card == 5:
        move("CC5",p,n)
    elif card == 6:
        move("CC6",p,n)
        
    elif card == 7:
        if n == "You":
            print("Please pay Parking Fines $30") #print result
            print("You now have $%d in you bank."%player_A[1])
        else:
            print("%s paid $30 Parking Fines."%n)
        p[1]-=30 #decrease money/value from the player's list, similar to card 9
    elif card == 8:
        if n == "You":
            print("You found $10 on the street!")
            print("You now have $%d in you bank."%player_A[1])
        else:
            print("%s found $10 on the street."%n)
            p[1]+=10 #increase money/value from the player's list, similar to card 10
    elif card == 9:
        if n == "You":
            print("Please pay $60 tax.")
            print("You now have $%d in you bank."%player_A[1])
        else:
            print("%s paid $60 tax."%n)
        p[1]-=60
    else:
        if n == "You":
            print("Happy birthday! Collect $100")
            print("You now have $%d in you bank."%player_A[1])
        else:
            print("It's %s's birthday! %s collected $100."%(n,n))
        p[1]+=100

#go for movement, p for player list, n for player name
def move(go,p,n):
    #tell the player taht they or the AIs are in jail and make thm miss one round
    if go == "JAIL":
        if p == player_A:
            print("You've arrived in JAIL.")
            player_A[4] = 1
            if player_A[3] < 1: #if the player doesn't have the 'GET OUT OF JAIL FREE' card
                print("You will miss the next round.")
            else:
                out = input("You have %d 'GET OUT OF JAIL FREE' card. Would you like to use one? (Y/N)\n>>>"%player_A[3]) #ask player if they want to use the special card they got from the chance station
                if out == "Y":
                    player_A[3] -= 1
                    print("You've used a card, so you will not miss the next round.")
                    Ajail.append(1)
                else:
                    print("You didn't use your card, you will miss the next round.")
        else:
            print("%s arrived in JAIL."%n)
            p[4] = 1
            if p[3] <1:
                print("%s will miss the next round."%n)
            else: #if the AI has a 'GET OUT OF JAIL FREE' card, computer will pick randomly if they want to use it or not
                out = random.randint(0,1)
                if out == 0:
                    print("%s didn't use their 'GET OUT OF JAIL FREE' card, they will miss the next round."%n)
                else:
                    p[3]-=1
                    print("%s used their 'GET OUT OF JAIL FREE' card, they will not miss the next round."%n)
                    if p == player_B:
                        Bjail.append(1)
                    elif p == player_C:
                        Cjail.append(1)
                    elif p == player_D:
                        Djail.append(1)

    #change players' positions and print out instructions for the chance station cards, similar for everything below
    elif go == "CC4":
        p[2] +=1
        if p == player_A:
            print("Please move forward one space.")
            print("You have arrived at %s." %(positions[player_A[2]%14]))
            print("Please pay $100 tax.")
            player_A[1]-=100
            print("You now have $%d in your bank account."%player_A[1])
        else:
            print("%s moved forward one space."%n)
            output(p,n)
    elif go == "CC5":
        p[2]-=3
        if p == player_A:
            print("PLease move backward three spaces.")
            print("You have arrived at %s." %(positions[player_A[2]%14]))
            buy(player_A,"A")
            pay_rent(player_A,"A")
        else:
            print("%s moved backward 3 spaces."%n)
            output(p,n)
    elif go == "CC6":
        p[2] = 0
        if p == player_A:
            print("Advance to GO.")
            print("You have arrived at %s." %(positions[player_A[2]%14]))
            player_A[1]+=200
            print("You received $200.")
            print("You now have $%d in your bank account."%player_A[1])
        else:
            print("%s advanced to GO."%n)
            output(p,n)
    else:
        dice(p,n) # if there are no special situations, call the dice funtion, the players will just roll the dice

#a function for purchasing houses
def buy(p,n):
    #if the house is not own by anyone, the players can buy them
    if positions[p[2]%14] not in PA_house and positions[p[2]%14] not in PB_house and positions[p[2]%14] not in PC_house and positions[p[2]%14] not in PD_house and p[2]%14 != 3 and p[2]%14 != 10 and p[2]%14 != 11 and p[2]%14 != 0:

        #Ask player if they would like to buy,skip or seee the map
        if p == player_A:
            print("Would you like to purchase this property? The cost is $%d." %(house_value[player_A[2]%14]))
            buy = input("You have $%d in your bank. Enter Y to purchase, N to skip or MAP to view the map.\n>>> "%player_A[1])
            if buy == "MAP":
                printMap()
                buy = input("Would you like to purchase this property? (Y/N)\n>>> ")
            if buy == "Y":
                player_A[1] -= house_value[player_A[2]%14] #decrease money
                PA_house[player_A[2]%14] = positions[player_A[2]%14] #add the house into the PA_house list to store it
                owner[player_A[2]%14] = 'A' #update the owner list so owner will print on the map
                #if the player bought the train station, tell them the special rule
                if player_A[2]%14 == 6:
                    print("You are now the owner of the Train Station, when other players come, they will be charged 12 times their dice value as the rent.")
                else:
                    just_bought[p[2]%14] +=1 #update the list so the next time they come back they can upgrade
                    print("You are now the owner of %s, when other players arrive in this house, they will be charges $%d. \nYou can upgrade your house to increase the rent when you come back again, up to 3 times."%(positions[player_A[2]%14],house_value[player_A[2]%14]*0.30))
            else:
                print("Okay!")
        else:
            #decision making for the AIs, depending on how much money they have
            if p[1] > 500:
                buy =1
            elif p[1] < 350:
                buy = 0
            else:
                buy = random.randint(0,1)
            if buy == 1:
                p[1]-=house_value[p[2]%14]
                if p[2]%14 != 6:
                    just_bought[p[2]%14] +=1
                if p == player_B:
                    owner[player_B[2]%14] = 'B' #update lists to store values
                    PB_house[p[2]%14] = positions[p[2]%14]
                elif p == player_C:
                    owner[player_C[2]%14] = 'C'
                    PC_house[p[2]%14] = positions[p[2]%14]
                elif p == player_D:
                    owner[player_D[2]%14] = 'D'
                    PD_house[p[2]%14] = positions[p[2]%14]
                print("%s now own the %s."%(n,positions[p[2]%14])) #tell player the AIs' actions
            elif buy == 0:
                print("%s didn't purchase this property."%n)
                
#a function for paying and recieving rent
def pay_rent(p,n):
    if p[2]%14 == 6:
        rent = p[0]%14*12 #rent is 12 times the current dice value for the train station, which is at position 6
    else:
        rent = house_value[p[2]%14]*0.3 #any other houses has a rent of 30% of the current house value
        
    if p != player_A: # if the current player is not Player A, then it means that the other players are paying Player A rent
        if positions[p[2]%14] in PA_house:
            p[1] -= rent #decrase money of the current player
            player_A[1] += rent #increase money for Player A
            print("%s paid you $%d rent."%(n,rent))
            print("You now have $%d."%player_A[1])
        else:
            #find the owner of the house and decrase the current player's money by the rent and add that value to the owner's list
            if positions[p[2]%14] in PB_house and p != player_B:
                o = "B"
                p[1] -= rent
                player_B[1] += rent
                print("%s paid Player %s $%d rent."%(n,o,rent))
            elif positions[p[2]%14] in PC_house and p != player_C:
                o = "C"
                p[1] -= rent
                player_C[1] += rent
                print("%s paid Player %s $%d rent."%(n,o,rent))
            elif positions[p[2]%14] in PD_house and p != player_D:
                o = "D"
                p[1] -= rent
                player_D[1] += rent
                print("%s paid Player %s $%d rent."%(n,o,rent))
        
    elif p == player_A: #Found out which player owns the house and make Player A pay them the rent
        if positions[p[2]%14] in PB_house: #check if the house is stored inside each player's house list
            p[1] -= rent
            player_B[1] += rent
            print("You have to pay %s $%d rent."%("Player B", rent))
            print("You now have $%d left."%player_A[1])
        elif positions[p[2]%14] in PC_house:
            p[1] -= rent
            player_C[1] += rent
            print("You have to pay %s $%d rent."%("Player C", rent))
            print("You now have $%d left."%player_A[1])
        elif positions[p[2]%14] in PD_house:
            p[1] -= rent
            player_D[1] += rent
            print("You have to pay %s $%d rent."%("Player D", rent))
            print("You now have $%d left."%player_A[1])

#a function to upgrade houses up to 3 times
def house_upgrade(p,n):
    if upgrade[p[2]%14] != 'x' and just_bought[p[2]%14] != 0 and upgrade[p[2]%14] <3: #check if the current position is a house(x means it's not a house.),check if the house was just bought this round, check if the house has been upgraded less than 3 times
        upgrade_cost = house_value[player_A[2]%14]*0.6 #calculate the upgrade cost,60% of the current house value
        if p == player_A and positions[p[2]%14] in PA_house:#check if player A owns the house
            up = input("Would you like to upgrade this house? The cost to upgrade is $%d and you have $%d.\nYou can increase your house value by 15 percent and the rent accordingly. You've upgraded this house %d times with %d times left. (Y/N) Or type MAP to view the map.\n>>> "%(house_value[player_A[2]%14]*0.6, player_A[1], upgrade[p[2]%14], 3-upgrade[p[2]%14]))
            if up == "MAP":
                printMap()
                up = input("Would you like to upgrade?(Y/N)\n>>>")
            if up == "Y":
                house_value[player_A[2]%14] *= 1.15 #update the house value in the list if player chose to upgrade.
                player_A[1] -= upgrade_cost #decrase player A's money by the cost
                upgrade[p[2]%14] += 1 #increase the house level, this will be shown on the map
                print("%s is upgraded, its current value is $%d, the rent has increased to $%d."%(positions[player_A[2]%14], house_value[player_A[2]%14]*1.15, house_value[player_A[2]%14]*0.3))
                print("You have $%d left."%player_A[1])
            else:
                print("Okay.")
        elif p != player_A:
            if positions[p[2]%14] in PB_house or positions[p[2]%14] in PC_house or positions[p[2]%14] in PD_house:
                o = 0
                if p == player_B and positions[p[2]%14] in PB_house: #check for the owner of the current house
                    o = "B"
                elif p == player_C and positions[p[2]%14] in PC_house:
                    o = "C"
                elif p == player_D and positions[p[2]%14] in PD_house:
                    o = "D"
                if o == "B" or o == "C" or o == "D":
                    if p[1] > house_value[p[2]%14]*0.6:#check if the current AI player has enough money to upgrade
                        up = random.randint(0,1) # ramdomly chose if they AI would upgrade
                    else:
                        up = 0
                    if up == 1:
                        house_value[p[2]%14] *= 1.15 #find the cost
                        p[1] -= upgrade_cost #update the list values
                        upgrade[p[2]%14] += 1
                        print("Player %s upgrade their %s."%(o,positions[p[2]%14]))
                    else:
                        print("Player %s didn't upgrade their house."%o)

    elif upgrade[p[2]%14] >= 3: #tell the player that te house has reached its maximum upgrade
        if p == player_A and positions[p[2]%14] in PA_house:
            print("You've upgraded this house 3 times, you cannot upgrade anymore.")
        else:
            if p == player_B and positions[p[2]%14] in PB_house:
                print("%s upgrade this house 3 times, %s cannot upgrade this house anymore."%(n,n))
            elif p == player_C and positions[p[2]%14] in PC_house:
                print("%s upgrade this house 3 times, %s cannot upgrade this house anymore."%(n,n))
            elif p == player_D and positions[p[2]%14] in PD_house:
                print("%s upgrade this house 3 times, %s cannot upgrade this house anymore."%(n,n))
                
                        
#Tell the current positions of players
def where_A():
    move(1,player_A,"A")
    if player_A[2]%14 !=3:
        print("You have arrived at %s." %(positions[player_A[2]%14]))
        if player_A[2]%14 != 0 and player_A[2]%14 != 6 and player_A[2]%14 != 10 and player_A[2]%14 != 11:
            house_upgrade(player_A,"A") #call the house_hupgrade function to alllow upgrade if the current position is a house
        buy(player_A,"A")#call the buy function to check if Player could purchase the current position
        if player_A[2]%14 !=0:
            pay_rent(player_A,"A") # call the pay_rent function to check if player need to pay rent
        if player_A[2]%14 == 10:
           chance_card(player_A,"You") #call the chance card function after player arrived in chance station
        elif player_A[2]%14 == 11:
            print("Please pay $100 tax.") #ask player to pay tax in tax bureau
            player_A[1]-=100 #update list, decrease money 
            print("You now have $%d in your bank account."%player_A[1])
        elif player_A[2]%14 == 0 and player_A[4] != 0:#check if player A has arrived at GO, and make sure it's not the first round when they all start at GO
            player_A[1]+=200 #increase list value
            print("You received $200.")
            print("You now have $%d in your bank account."%player_A[1])
        elif player_A[4]%14 > player_A[2]%14:#check if player A has just past GO, if the previous position index is larger than the current position index
            player_A[1]+=200 #increase list value
            print("You've past GO and received $200.")
            print("You now have $%d in your bank account."%player_A[1])


#Generate AI positions and actions
def where_AI(n):
    if n == "Player B":
        move(1,player_B,"Player B") #generate AI movements by calling move function
        output(player_B,n)#call the ouput function with variables it needs
    elif n == "Player C":
        move(1,player_C,"Player C")
        output(player_C,n)
    elif n == "Player D":
        move(1,player_D,"Player D")
        output(player_D,n)
#ouputs the actions of AI to the screen
def output(p,n):
    if p[2]%14 != 3:
        print("%s arrived at %s."%(n,positions[p[2]%14])) #output the position of AIs if they are not in jail
        if p[2]%14 != 0 and p[2]%14 != 6 and p[2]%14 != 10 and p[2]%14 != 11:#check if current position is a house
            house_upgrade(p,n) #call the house_upgrade function so AIs can upgrade their houses
        buy(p,n)#call the buy function to check if it's possible to purchase the current property
        pay_rent(p,n) #call the pay_rent function to check if the current player needs to pay rent
        if p[2]%14 == 10:
            chance_card(p,n) #call the chance card function if player arrived in position 10, chance station
        #similar to where_A function above
        elif p[2]%14 == 11:
            print("%s paid $100 tax."%n)
            p[1]-=100 
        elif p[2]%14 == 0:
            p[1]+=200
            print("%s received $200."%n)
        elif p[4]%14 > p[2]%14 :
            p[1]+=200
            print("%s past GO and received $200."%n)

#start the game function
def start():
    print("Each player will roll a dice, the player with the highest number go first and the others goes alphabetically.\nIf more the one person has the highest number, A goes before B, C goes before D etc.")
    time.sleep(0.5)
    input("\nPlayer A, please roll the dice. Type any letter/number or press Enter to roll.\n>>> ")
    #pick random values from 1 to 6 for each player
    A = random.randint(1,6)
    print("You rolled %d" %A)
    B = random.randint(1,6)
    C = random.randint(1,6)
    D= random.randint(1,6)
    print("Player B rolled %d"%B)   
    print("Player C rolled %d"%C)
    print("Player D rolled %d"%D)
    #find the highest number of the 4 players
    first = max(A,B,C,D)
    #tell player who will be able to roll first and call the order function
    if A == first:
        print("You go first.\n")
        order("A")
    elif B == first:
        print("Player B goes first.\n")
        order("B")
    elif C == first:
        print("Player C goes first.\n")
        order("C")
    elif D == first:
        print("Player D goes first.\n")
        order("D")

#controlls the order of players rolling the dice, x for the list of the player who roll the highest number in the start function
def order(x):
    #check if the players are broke or not before starting a new round of dice rolling
    if player_A[1] <= 0:
        player_A[1] = 0
        print("\n\nYou are broke, you lost the game. \n")
        compare() #if a player is broke, call the compare function for the result
    elif player_B[1] <= 0:
        player_A[1] = 0
        print("\n\nPlayer B is broke and lost the game. \n The game is over.")
        compare()
    elif player_C[1] <= 0:
        player_A[1] = 0
        print("\n\nPlayer C is broke and lost the game. \n The game is over.")
        compare()
    elif player_D[1] <= 0:
        player_A[1] = 0
        print("\n\nPlayer D is broke and lost the game. \n The game is over.")
        compare()
    else:
        #if the game continues, keeps asking players to roll the dice in order
        if x == "A":
            where_A()#calls Player A's function 
            where_AI("Player B")#calls the AI's function
            where_AI("Player C")
            where_AI("Player D")
        elif x == "B":
            where_AI("Player B")
            where_AI("Player C")
            where_AI("Player D")
            where_A()
        elif x == "C":
            where_AI("Player C")
            where_AI("Player D")
            where_A()
            where_AI("Player B")
        elif x == "D":
            where_AI("Player D")
            where_A()
            where_AI("Player B")
            where_AI("Player C")
        order(x) #repeat and loop the function order


#a function to compare the total value of each player if the gme ends
def compare():
    #create new local variables
    A_house_total = 0
    B_house_total = 0
    C_house_total = 0
    D_house_total = 0
    #check for houses in each player's house list
    for i in PA_house:
        if i != 0:#if there is a house
            A_house_total += house_value[PA_house.index(i)] #find the corresponding house value and add it to the local house total value list above
    for i in PB_house:
        if i != 0:
            B_house_total += house_value[PB_house.index(i)]
    for i in PC_house:
        if i != 0:
            C_house_total += house_value[PC_house.index(i)]
    for i in PD_house:
        if i != 0:
            D_house_total += house_value[PD_house.index(i)]

    #find the total value of each player by adding the total house value with the money of each player
    A_total_value = A_house_total + player_A[1]
    B_total_value = B_house_total + player_B[1]
    C_total_value = C_house_total + player_C[1]
    D_total_value = D_house_total + player_D[1]

    #find the highest value in the 4 players' totals
    win = max(A_total_value,B_total_value,C_total_value,D_total_value)

    #output the totals to the screen
    print("All player's houses has been converted into cash money.")
    print("You have $%d in total."%A_total_value )
    print("Player B has $%d in total."%B_total_value )
    print("Player C has $%d in total."%C_total_value )
    print("Player D has $%d in total."%D_total_value )

    #fin the winner and output the result
    if A_total_value == win:
        print("\nYOU WON!!!")
    elif B_total_value == win:
        print("\nPlayer B WON!")
    elif C_total_value == win:
        print("\nPlayer C WON!")
    elif D_total_value == win:
        print("\nPlayer D WON!")


#The very beginning------
#Print the title of the game
print(" ")
print("""

                           _    _        _                                          _          
                          | |  | |      | |                                        | |         
                          | |  | |  ___ | |  ___   ___   _ __ ___    ___           | |_   ___  
                          | |/\| | / _ \| | / __| / _ \ | '_ ` _ \  / _ \          | __| / _ \ 
                          \  /\  /|  __/| || (__ | (_) || | | | | ||  __/          | |_ | (_) |
                           \/  \/  \___||_| \___| \___/ |_| |_| |_| \___|           \__| \___/ 
                                                                                               
                                                                                               

""")
time.sleep(0.3)
print("""

                        █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄             █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █░░ █░░█
                        █░░█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█             █░▀░█ █░░█ █░░█ █░░█ █░░█ █░░█ █░░ █▄▄█
                        █▀▀▀ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀             ▀░░░▀ ▀▀▀▀ ▀░░▀ ▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀ ▄▄▄█

""")
time.sleep(0.6)
#ask player if they want to start the game
ready = input("\n\nR U READY ? (Y/N) \n>>> ")

if ready == "Y":
    print("You are PLAYER A, and you will be playing against 3 other players.")
    if (input("\nWould you like to see the rules? (Y/N) \n>>> ") == "Y" ): #ask player if they want to so the rules, if yes, print the rules
        print('''
The object of the game is to become the richest person in the town, the game ends when one of the players is broke.

Game Rules

- Everyone starts on the space that says “GO”, each player rolls the dice, the player with the largest number goes first, the others will go in alphabetical order.
- Everytime you go pass “GO”, you will receive $200.
- Whenever you land on a space that no one owns you may buy the land/house.
- Anyone who lands on your space will be charged a 30% of your house’s current value and the rent, when you land on your house, you may choose to upgrade. 
- A house could upgrade up to three times, after each upgrade the map indicate the number of times the house was upgraded(1,2,3).
- The cost to upgrade is 60% of the house’s current value, value of house will increase by 15% after each upgrade.
- If you own the train station, the player who land in the station will have to pay 12 times the number on their dice.
- If you get into jail, you will miss one round, but nothing else will be affected.
- If you land on the space that says “Chance” you will have to pick a random card.
- When the game ends(when one player has no more money), houses will convert to cash according to their current value, the player with the most money wins.\n
        ''')
        if (input("Let's start the game! (Y/N) \n>>> ") == "Y"): #ask if they want to start
            print("\nHere is the map.")
            printMap()#call the printMap function to output the map
            print("\nEvery player starts at GO")
            start()#call the start function to begin the game
        else:
            print("Okay Bye!")
    else:#if the player chose not to see the rules, ask them if they want to start and call the printMap function
        print("\nHere is the map.")
        printMap()
        print("Every player starts at GO")
        start()
else:
    #if the player does not want to play the game
    print("Bye!")
