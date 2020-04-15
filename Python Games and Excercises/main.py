from tkinter import Tk, Label, Button, Frame, PhotoImage
from Player import Player, card
import random, time

class BlackJack:
  def __init__(self, master):

    self.player = Player()
    self.dealer = Player(dealer=True)
    self.master = master
    master.title("Blackjack")   

    self.hand = []
    self.dealer_hand = []
    self.deck = []

    self.set_cards()
  
  #Frames
    self.dealer_frame = Frame(master)
    self.dealer_frame.grid(row = 0, column = 0)

    self.player_frame = Frame(master)
    self.player_frame.grid (row = 1, column = 0)

    self.win_frame = Frame(master)
    self.win_frame.grid (row = 2, column = 0)

    self.buttons_frame = Frame(master)
    self.buttons_frame.grid (row = 3, column = 0)

  #Labels
    self.label_dealer = Label(self.dealer_frame, text = "WELCOME TO BLACKJACK~\n\nDealer is waiting...", fg="blue")
    self.label_dealer.grid(row = 1, column = 0)

    self.label_player = Label(self.player_frame, text = "Press Deal to start!", fg = "blue")
    self.label_player.grid(row = 1, column = 0)

    self.label_win = Label(self.win_frame, text = "")
    self.label_win.grid(row = 1, column = 0)

  #Buttons
    self.deal_button = Button(self.buttons_frame, text = "Deal", command = self.deal)
    self.deal_button.grid(row = 0, column = 0)

    self.hit_button = Button(self.buttons_frame, text = "Hit", command = self.hit, state = 'disabled')
    self.hit_button.grid(row = 0, column = 1)

    self.stand_button = Button(self.buttons_frame, text = "Stand", command = self.stand, state = 'disabled')
    self.stand_button.grid(row = 0, column = 2)

#Generate card graphics
  def set_cards(self):
    for letter in ["C","D","H","S"]:
      for number in range(1,14):
        filename = "cards//%s%s.png" % (number,letter)
        if number > 10:
          value = 10
        else:
          value = number
        self.deck.append(card(filename,value))

    random.shuffle(self.deck)

  def new_card(self):
    sum = 0
    new = self.deck[0]
    self.hand.append(new)
    self.deck.pop(0)
    photo = PhotoImage(file = new.filename)
    new.label = Label(self.player_frame, image=photo)
    new.label.photo = photo

    #refresh the screen and add an image for each card
    for card in self.hand:
      sum += card.value
      card.label.grid(row = 0, column = self.hand.index(card))

      self.label_player.config(text="Player Total: %d" %sum)
    return sum
      

  def new_card_dealer(self):
    sum = 0
    new = self.deck[0]
    self.dealer_hand.append(new)
    self.deck.pop(0)
    photo = PhotoImage(file = new.filename)
    new.label = Label(self.dealer_frame, image=photo)
    new.label.photo = photo

    #refresh the screen and add an image for each card
    for card in self.dealer_hand:
      sum += card.value
      card.label.grid(row = 0, column = self.dealer_hand.index(card))

      self.label_dealer.config(text="Dealer Total: %d" %sum)
    return sum


  def deal(self):
    self.deal_button.config(state='disabled')
    self.hit_button.config(state='normal')
    self.stand_button.config(state='normal')

    #give dealer cards
    self.new_card_dealer()
    self.dealer.sum = self.new_card_dealer()

    #give player cards
    self.new_card()
    self.player.sum = self.new_card()

    self.label_dealer.config(text="Dealer's Cards")

    self.label_player.config(text="Player Total: %d" % self.player.sum)
    
    self.label_win.config(text ="")

  def hit(self):
    #add a new random cards
    self.player.sum = self.new_card()

    #update label_player so it says something like "you drew x, your total is y"
    self.label_player.config(text="Player Total: %d" % self.player.sum)

    if self.player.sum > 21:
      #    update label_win with a loss message
      self.label_win.config(text="Player Busts! \nYOU LOSE!",fg = "red")
      #     disable the hit and stand buttons
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      #    call the self.reset() function after 2 seconds
      self.master.after(2000,self.reset)

  def stand(self):
    # disable all buttons
    self.deal_button.config(state='disabled')
    self.hit_button.config(state='disabled')
    self.stand_button.config(state='disabled')

    # call the self.dealer_hit() function 
    self.dealer_hit()

  def dealer_hit(self):
    # this function will handle the dealer AI recursively
    self.dealer.sum = self.new_card_dealer()

    if (self.dealer.sum > self.player.sum or self.dealer.sum == 21)and self.dealer.sum <= 21:
      #update label_win with a loss message
      self.label_dealer.config(text="Dealer Total: %d" % self.dealer.sum)
      self.label_win.config(text="DEALER WINS!", fg = "red")
      #     disable the hit and stand buttons
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      #    call the self.reset() function after 2 seconds
      self.master.after(2000,self.reset)      
    elif self.dealer.sum > 21:
      #update label_win with a WIN message
      self.label_win.config(text="Dealer Busts! \nYOU WIN!", fg = "orange")
      #     disable the hit and stand buttons
      self.hit_button.config(state='disabled')
      self.stand_button.config(state='disabled')
      #    call the self.reset() function after 2 seconds
      self.master.after(2000,self.reset)
    else:
      self.label_dealer.config(text="Dealer Total: %d" % self.dealer.sum)
      #    call the dealer.hit() function after 2 seconds
      self.master.after(2000,self.dealer_hit)

  def reset(self):
    #disable the hit and stand buttons
    self.hit_button.config(state='disabled')
    self.stand_button.config(state='disabled')

    #enable the deal button
    self.deal_button.config(state='normal')

    #reset all variables
    self.player.sum = 0 
    self.dealer.sum = 0
    
    self.hand =[]
    self.dealer_hand = []

    #destroy and recreat the frames (and labels)
    self.dealer_frame.destroy()
    self.player_frame.destroy()
    self.win_frame.destroy()

    self.dealer_frame = Frame(self.master)
    self.dealer_frame.grid(row = 0, column = 0)

    self.player_frame = Frame(self.master)
    self.player_frame.grid (row = 1, column = 0)

    self.win_frame = Frame(self.master)
    self.win_frame.grid (row = 2, column = 0)

    #Labels
    self.label_dealer = Label(self.dealer_frame, text="WELCOME TO BLACKJACK~\n\nDealer is waiting...", fg="blue")
    self.label_dealer.grid(row = 1, column = 0)

    self.label_player = Label(self.player_frame, text="Press Deal to start!",fg="blue")
    self.label_player.grid(row = 1, column = 0)

    self.label_win = Label(self.win_frame, text = "")
    self.label_win.grid(row = 1, column = 0)
    
    
    

root = Tk()
my_gui = BlackJack(root) #creates the BlackJack instance
root.mainloop()
