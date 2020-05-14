
import random

suits = ('♣', '♦', '♥', '♠')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
        'Queen':10, 'King':10, 'Ace':11}


deck = []
playing = True





class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return(self.rank + self.suit)
        


class Deck :

    def __init__(self):
        

        # start with an empty list
        for suit in suits:
            for rank in ranks:
                deck.append (Card(suit,rank))


    def __str__(self):
        b = []
        i = 0 
        while i < len(deck):
            b.append('{}'.format(deck[i]))
            i+=1

        return str (b) 
        return b


    def __getitem__(self,index):
        return deck[index]

    def shuffle(self):
        random.shuffle(deck)

    def deal(self):
        x = 0 
        if x < len(deck):
            Card = ((deck.pop()))
            return Card

class Hand (Deck):
    
    def __init__(self):
        #Deck.__init__(self)
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        
    
    def add_card(self,Deck):
        Deck.shuffle()
        g = Deck.deal()
        
        self.value = self.value + (values.get(g.rank))
        self.cards.append((  str(g)     ))
        return (self.cards, 'Your count is {}'.format(self.value))
    
    def __str__(self):
        b = []
        i = 0 
        while i < len(self.cards):
                b.append('{}'.format(self.cards[i]))
                i+=1
        return str (b)
    
    def __getitem__(self,index):
        return self.cards[index]
        
    def adjust_for_ace(self):
        for i in range (0,len(self.cards)):
            if self.value >= 21 and ('Ace' in self.cards[i]):
                print ('True')
                self.value -= 10
                print(self.value, 'adjust for ace')
            i+=1
                

class Chips:
    
    def __init__(self):
        self.total = 100  
        self.bet = 0
        
    
    def total(self):
        return self.total
    def win_bet(self):
        self.total = self.total + (2*self.bet)
    
    def lose_bet(self):
        self.total = self.total 



c = Chips()



c.total





def take_bet(Chips):
     
    while True:
        try:
            bet = int(input('Please enter a number to place your bet'))
            if (type(bet)) == int and (bet < Chips.total):
                Chips.bet = bet
                print('thanks')
                Chips.total = Chips.total - Chips.bet
                return Chips.bet
        except TypeError:
            print('this will  not work ')
            continue
            
        except ValueError:
            print('this will  not work ')
            continue
            
        else:
            print('you got your answer mate')
            break
    
    

def hit(Deck,Hand):
    if Hand == Player_Hand and Hand.value>21:
        Hand.adjust_for_ace()
        if Hand.value < 21:
            Hand.add_card(Deck)
            print (Hand.value,'ph')
    elif Hand == Player_Hand and Hand.value<21:
        Hand.add_card(Deck)
        print (Hand.value,'ph')
    
    
    if Hand == Dealer_Hand and Hand.value<=17:
        print (Hand.value,'ph')
        Hand.add_card(Deck)





def hit_Player(Deck,Hand):
    if Hand.value>21:
        Hand.adjust_for_ace()
        if Hand.value < 21:
            Hand.add_card(Deck)
            
    elif Hand.value<21:
        Hand.add_card(Deck)
         



def hit_Dealer(Deck,Hand):
    if  Hand.value<=21:
        print (Hand.value)
        Hand.add_card(Deck)




def hit_or_stand(Deck,Hand):
    global playing 
    Player = input('Do you want to hit, type Y or N')
    if Player.upper() == 'Y':
        hit_Player(Deck,Hand)
    elif Player.upper() == 'N':
        playing = False
    



def replay_no():
    deck = []
    global playing 
    playing = False





def replay_yes():
    deck = []
    global playing
    playing = True





def show_some(Player_Hand,Dealer_Hand):
    print ('PLAYER: {} {}'.format(Player_Hand,Player_Hand.value), 'DEALER: {} {}'.format(['??'] + Dealer_Hand.cards[1:],Dealer_Hand.value))
   
    
def show_all(Player_Hand,Dealer_Hand):
    print ('PLAYER: {} {}'.format(Player_Hand,Player_Hand.value), 'DEALER: {} {}'.format(Dealer_Hand,Dealer_Hand.value))



def player_busts(Player_Hand,Player_Chips):
    if Player_Hand.value > 21 or Player_Chips.total <= 0:
        Player_Chips.lose_bet()
        print ('PLAYER BUST')
        return True 
    else:
        return False
            

def player_wins(Player_Hand,Dealer_Hand,Player_Chips):
    if (abs(Player_Hand.value - 21) < abs(Dealer_Hand.value - 21)) and (Player_Hand.value <= 21) and (Dealer_Hand.value <= 21):
            print ('PLAYER WINS')
            Player_Chips.win_bet()
            return True 
    else:
        return False
    

def dealer_busts(Dealer_Hand,Player_Hand,Player_Chips):
    if (Dealer_Hand.value > 21) and Player_Hand.value <= 21:
        print ('DEALER BUSTS')
        Player_Chips.win_bet()
        return True 
    else:
        return False
        
    
def dealer_wins(Dealer_Hand,Player_Hand,Player_Chips):
    if (abs(Player_Hand.value - 21) > abs(Dealer_Hand.value - 21)) and (Player_Hand.value <= 21) and (Dealer_Hand.value <= 21):
        print ('DEALER WINS')
        Player_Chips.lose_bet()
        return True 
    else:
        return False
    
      
def push(Dealer_Hand,Player_Hand,Player_Chips):
    if (Player_Hand.value ==  Dealer_Hand.value) and (Player_Hand.value) <= 21 and (Dealer_Hand.value <= 21):
        print ('PUSH')
        return True 
        Player_Chips.total = Player_Chips.total + Player_Chips.bet
    else:
        return False
    


def black ():
    global playing 
    playing = True
    Player_Chips = Chips()
    
    
    print ('LETS PLAY BLACK JACK!')

    while playing == True: 
        
        D1 = Deck()
        D1.shuffle()
        Dealer_Hand = Hand()
        Player_Hand = Hand()
        Dealer_Hand.add_card(D1)
        Player_Hand.add_card(D1)
        print('Your total is',Player_Chips.total)

        



        # Prompt the Player for their bet
        take_bet(Player_Chips)
        print('Your total is now',Player_Chips.total)


        # Show cards (but keep one dealer card hidden)
        show_some(Player_Hand,Dealer_Hand)


        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(D1,Player_Hand)

            # Show cards (but keep one dealer card hidden)
            show_some(Player_Hand,Dealer_Hand)


            # If player's hand exceeds 21, run player_busts() and break out of loop
            player_busts(Player_Hand,Player_Chips)
            if player_busts(Player_Hand,Player_Chips) == True:
                print ('Your total is {}'.format(Player_Chips.total))
                replay = input('play again')
                if replay.upper() == 'Y':
                    replay_yes()
                    break
                else:
                    replay_no()
                    break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while player_busts(Player_Hand,Player_Chips) == False:
            if Dealer_Hand.value <= 17:
                hit_Dealer(D1,Dealer_Hand)


            # Show all cards
            show_all(Player_Hand,Dealer_Hand)


            # Run different winning scenarios
            player_wins(Player_Hand,Dealer_Hand,Player_Chips)
            dealer_busts(Dealer_Hand,Player_Hand,Player_Chips)
            dealer_wins(Dealer_Hand,Player_Hand,Player_Chips)
            push(Dealer_Hand,Player_Hand,Player_Chips)
            if player_wins(Player_Hand,Dealer_Hand,Player_Chips) == True or dealer_busts(Dealer_Hand,Player_Hand,Player_Chips) == True or dealer_wins(Dealer_Hand,Player_Hand,Player_Chips) == True or push(Dealer_Hand,Player_Hand,Player_Chips) == True:
                print ('Your total is {}'.format(Player_Chips.total))
                replay = input('play again')
                if replay.upper() == 'Y':
                    replay_yes()
                    break
                else:
                    replay_no()
                    break


        # Inform Player of their chips total 
    print ('Your total is {}'.format(Player_Chips.total))


    















black()

















