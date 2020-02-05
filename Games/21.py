# 21
import random

p_card1 = random.randint(2,11)
p_card2 = random.randint(2,11)
p_total = p_card1 + p_card2
d_card1 = random.randint(2,11)
d_card2 = random.randint(2,11)
d_total = d_card1 + d_card2
p_card_new = 0
d_card_new = 0

print("Welcome\n\nYou drew %d and %d and your total is %d\nDealer drew %d and the other one is hidden"%(p_card1,p_card2,p_total,d_card1))
choice = input("Hit or Stay? \n>>> ")

while choice == "hit" and p_total <= 21:
    p_card_new = random.randint(2,11)
    p_total += p_card_new
    print("You drew %d, total is %d"%(p_card_new,p_total))
    if p_total <= 21:
        choice = input("Hit or Stay? \n>>> ")

if p_total > 21:
    print("You lose")
