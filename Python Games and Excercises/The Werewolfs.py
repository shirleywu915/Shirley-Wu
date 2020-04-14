"""
Name: Shirley Wu
Date: October 26, 2018
Choose Your Own Adventure assignment: 

SAVE THE VILLAGE!!!

1: Witch/Wizard
2: Villager
3: Werewolf
4: Werewolf
5: Fortune Teller
6: Villager

* But nobody except themselves know these identities, they’ll have to guess and analyze with logic *
"""
print("""Oh no! There are 6 people locked inside a room.

There are:
           -- 2 Werewolves
                   (They will kill one person every night, they only know the identity of each other)
           -- 1 Fortune Teller
                   (He or she can check one person's identity every night)
           -- 1 Witch/Wizard
                   (He or she has one bottle of poison and one bottle of antidote. He or he can choose to save the person who was just killed by the werewolves on the same night with his/her antidote, or kill a person who he/she thinks is a werewolf at night with her poison, both of the bottles cannot be used all in one night.)
           -- 1 Villager
                   (Have no special power, he or she can only use logic and try to find out who the werewolves are)

Your job is to kill both of the werewolves in the morning before all the other three people are killed to save the village. You will have to read/listen to what each person says and guess who the werewolves are.""")

name = input("What is your name?\n>>> ")
start = input("\nR U READY %s?(Y or N)\n>>> " %name)
if (start == "Y" or start == "y"):
   print("Let's go!!\n..")
else:
   print("Let's go anyways!!\n...")

print("""The first night passed, and player 2 was killed...
Now is time for each person to speak...

Player 1: "Since player 2 just died, then he is definitely not a werewolf. Well, I don't know who you all are, but I am someone with special power."

Player 3: "I am just a regular villager, I don't have much to say."

Player 4: "I am the fortune teller, and last night I checked player 6's identity and she is a werewolf."

PLayer 5: "I am not a werewolf, I think that player 3 could be a werewolf because he didn't know what to say, and he looks calm like he knew he wouldn't be killed last night."

Player 6: "I am a villager, NOT A WEREWOLF, I agree with what player 5 said, and I think player 1 is suspicious also. So I think we should get rid of player 3 first, and then can the fortune teller check out player 1's identity at night?"

""")

first_day = int(input("So who do you want to kill first? (Enter 1, 3, 4, 5, or 6)\n>>> "))
if (first_day == 1):
   print("""You have killed Player 1. This night, Player 6 was killed...
Now is time for each person to speak...

Player 3: "Well, I don't understand why would the werewolves kill Player 6 if she is just a villager... Anyway, I think Player 1 could be a werewolf because he just said he had special but didn't say what it was. I hope the Player 4 could tell us who he checked out last night and help us out."

Player 4: "WHY DIDN'T YOU KILL PLAYER 6 %s!!! I SAID SHE IS A WEREWOLF!!! Last night I checked Player 3, and he is not a werewolf."

Player 5: "Wow... You are such a good actor Player 4! He is a werewolf, I am the real fortune teller, and I checked player 1 the first night and she is not a werewolf, and last night I found out that Player 3 is a werewolf. But, it's too late now... I am going to be killed tonight, %s you've made the wrong choice."

""" %(name,name))
   second_day_a = int(input("So who do you want to kill? (Enter 3, 4 or 5)\n>>> "))
   if (second_day_a == 3):
       print("You killer player 3, and player 5 was killed at night. Werewolves win, you didn't save the village.")
   elif (second_day_a == 4):
       print("You killer player 4, and player 5 was killed at night. Werewolves win, you didn't save the village.")
   elif (second_day_a == 5):
       print("You killer player 5. Werewolves win, you didn't save the village.")
   else:
       print("Invalid input")

elif (first_day == 3):
   print(""""You killed player 3. This night, player 5 was killed...
Now is time for each person to speak...

Player 1: "Both player 5 and 2 are not a werewolf, because they were killed at night by the werewolves. They are not killed by the witch/wizard because only one person died each night, so it's not possible for the witch to use her poison because he or she cannot use both the poison and antidote all in one night. I think player 4 should be the werewolf."

Player 4: "Last night I checked player 1's identity and he is a werewolf, therefore, %s, you should kill him."

Player 6: "I'm confused, sorry %s I can't help you..."

"""%(name,name))
   second_day_b = int(input("So who do you want to kill? (Enter 1, 4 or 6)\n>>> "))
   if (second_day_b == 1):
       print("You killed player 1, and player 6 was killed last night. Werewolves win, you didn't save the village.")
   elif (second_day_b == 4):
       print("Both the werewolves, are killed, you saved the village. Congratulation!")
   elif (second_day_b == 6):
       third_day_a = int(input("""You killed player 6. No one died on last night...
Now is time for each person to speak...

Player 1: "I'm the wizard, I saved myself with the antidote last night. And now it's clear that player 4 is a fake fortune teller, he is the werewolf!"

Player 4: "I AM THE REAL WIZARD, I said I was the fortune teller before because I wanted to protect the real fortune teller from the werewolf, trust me..."

So, %s who do you want to kill? (Enter 1 or 3)
>>>
""" %name))
       if (third_day_a == 1):
           print("You killed player 1, and player 6 was killed last night. Werewolves win, you didn't save the village.")
       elif (third_day_a == 3):
           print("You killed player 3, all the werewolves are dead. You saved the village. Congrats!")

elif (first_day == 4):
   print(""""You have killed player 4. This night, player 6 was killed...
Now is time for each person to speak...

Player 1: "There could be two possibilities for this result... First, Player 4 said that he is a fortune teller, he said he checked player 6 who is a werewolf, yet player 6 was killed tonight. Therefore, Player 4 could be a werewolf who tries to make us believe that player 6 is a werewolf. Or, Player 4 could be telling the truth and Player 6 attacked himself to trick the witch/wizards into using the antidote but didn't succeed. Just remember, I am someone with special power." 

Player 3: "I think that player 4 might have been a wizard, but he was killed by %s so he couldn't save himself with his antidote. Also, I think Player 1 could be a werewolf because he kept on saying that he has a special power, but never told us what it is."

PLayer 5: "I am the real fortune teller, I checked Player 6 the first night, and she is not a werewolf, and since Player 4 said he is a fortune teller, I checked on him last night and he is a werewolf. Also, I agree with what player 1 said, so I think player 3 is suspicious."
""" % name)
   second_day_c = int(input("So who do you want to kill? (Enter 1, 3 or 5)\n>>> "))
   if (second_day_c == 1):
       print("You killed PLayer 1, and player 5 was killed at night. Werewolves win, you didn't save the village.")
   elif (second_day_c == 3):
       print("Both the werewolves, are killed, you saved the village. Congratulation!")
   elif (second_day_c == 5):
       print(""""You killed PLayer 1. No one died last night...
Now is time for each person to speak...

Player 1: "I'm the wizard, I saved myself with the antidote last night. Player 3 has to be the werewolf, and he has been protecting Player 4, so they both werewolves."

Player 3: "I AM THE REAL WIZARD, I said that I'm just a villager at first because I don't want the werewolves to know I that had a special power."
""")
       third_day_b = int(input("So who are you going to kill? (Enter 1 or 3)\n>>>"))
       if (third_day_b == 1):
           print("You killed player 1. Werewolves win, you failed to save the village.")
       elif (third_day_b == 3):
           print("You killed player 5... Congratulation, you saved the village!")
       else:
           print("Invalid input")
   else:
       print("Invalid input")

elif (first_day == 5):
   print(""""You killed player 5. This night, no one was killed...
Now is time for each person to speak...

Player 1: "Nobody died last night, it must mean that the witch/wizard use their antidote. Or, maybe I use it to save myself~ Why don't you guess hahaha"

Player 3: "Why is Player 1 so relax, is it because he is a werewolf?"

PLayer 4: "I am the wizard, and I save Player 3 last night because I think he doesn't look like a werewolf."

Player 6: "I think Player 4 is very suspicious, Player 3 said he is just a village, so why would he use up his one and only antidote on a village, instead of saving it for himself or for the person with special power? Also, both Player 3 and 4 looks very relax too, I think we should kill player 4, by the way, I am the one and only villager, so who are you Player 3?"
""")
   second_day_d = int(input("So who do you want to kill? (Enter 1, 3, 4 or 6)\n>>>"))
   if (second_day_d == 1):
       print("You killed Player 1, and Player 6 died at night. You failed to save the village.")
   elif (second_day_d == 3):
       print("You killed Player 3, and Player 4 and 6 died at night, you saved the village! (FYI: The werewolf and the wizard killed each other.)")
   elif (second_day_d == 4):
       print("""You killed Player 4, and Player 1 died at night.
Now is time for each person to speak...

Player 3: "I AM NOT A WEREWOLF. Believe me %s!"

Player 6: "Just remember what I said last time %s, I am really just a villager."
""" %(name,name))
       third_day_c = int(input("So, %s who do you want to kill?\n>>> "%name))
       if (third_day_c == 3):
           print("You killed Player 3, both of the werewolves are killed, you saved the village. Good job!")
       elif(third_day_c == 6):
           print("You killed Player 6, werewolves win, you didn't save the village.")
       else:
           print("Invalid input")
   elif (second_day_d == 6):
       print("You killed Player 6, and Player 1 died at night. You failed to save the village.")
   else:
       print("Invalid input")
elif (first_day == 6):
   print(""""You killed Player 6. This night, No one was killed...
Now is time for each person to speak...

Player 1: "I know that if I tell all of you who I am I might get killed by the werewolves tonight, but I think I should still tell you... I am the Wizard, and last night, I saved myself. Remember, I still have a bottle of poison, so if you think someone is suspicious, tell me and I'll kill them tonight."

Player 3: "I don't have any special power, but my instinct tells me to trust Player 1."

Player 4: "I trust Player 1 too, I checked his identity last night and he is not a werewolf. Remember %s, I am a fortune teller."

Player 5: "I agree with Player 1 too. This is so funny, everybody trusted Player 1, including YOU, Player 4, the WEREWOLF. I am the REAL fortune teller, and I checked Player 1 on the first night and he is not a werewolf. Last night, I checked Player 4, and he is a werewolf, so, %s, if you kill player 4 now, and I'll check on Player 3 tonight, or the wizard could just kill him, then we will save the village!"
"""%(name,name))
   third_day_d = int(input("So who are you going to kill %s? (Enter 1, 3, 4, or 5)\n>>>"%name))
   if (third_day_d == 1):
       print("You killed Player 1, and Player 5 was killed at night, you failed to save the village.")
   elif (third_day_d == 3):
       print("You killed Player 3. At night, Player 4 and 5 died, you saved the village! (FYI: The wizard used their poison.)")
   elif (third_day_d == 4):
       print("You killed Player 4, and Player 3 and 5 was killed at night. Both the werewolves are dead, congrats!")
   elif (third_day_d == 5):
       print("You killed Player 5, Player 1 died at night. Werewolves win, you fail to save the village.")
else:
   print("Invalid input")


