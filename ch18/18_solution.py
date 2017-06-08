#! /usr/bin/python
import random

class Card(object):
  """ Represents a standard playing card"""
  def __init__(self,suit=0,rank=2):
    self.suit=suit
    self.rank=rank
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None,'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
  def __str__(self):
    return ('%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit]))
  def __cmp__(self,other):
    t1=self.suit,self.rank
    t2=other.suit,other.rank  
    return cmp(t1,t2) 
class Deck(object):
  def __init__(self):
    self.cards=[]
    for suit in range(4):
      for rank in range(1,14):
        card=Card(suit,rank)
        self.cards.append(card)
  def move_cards(self,hand,num):
    for i in range (num):
      hand.add_card(self.pop_card())  
    
  def __str__(self):
    res=[]
    for card in self.cards:
      res.append(str(card))
    return '\n'.join(res)
  def pop_card(self):
    return self.cards.pop()
  def add_card(self,card):
    self.cards.append(card)
  def shuffle(self):
    random.shuffle(self.cards)
  def sort(self):
    sort.self.cards()
  def move_cards(self,hand,num):  # 
    for i in range(num):
      hand.add_card(self.pop_card())
  def deal_hands(self, num_of_hands, cards_per_hand):
    for hand_count in range(num_of_hands):
            # Create hand and label based on index
      hand_name = 'hand_num' + str(hand_count)
      hand = Hand(hand_name)
      print
      print "Created hand called", hand_name
      for card_count in range(cards_per_hand):
                # Pop cards into hand from the deck
        hand.add_card(self.pop_card())
        print "Hand has cards"
        print hand
        print "#" * 30

    
    
class Hand(Deck):  # inheritance derived class Hand by Deck
  """ Represents hand of playing"""
  def __init__(self,label=''):
    self.cards=[]
    self.label=label

   #now we can use methods pop_card,add_card for Hand and Deck 
   #__init__() changes bcz 52 with empty list ?
card1=Card(3,8)
card2=Card(1,2)
print(card1)
a=Deck()
print(a)
# inheritance mode starts
hand=Hand('new Hand')
print (hand.cards)
print(hand.label)
deck=Deck()
#card=deck.pop_card()
#hand.add_card(card)
#print hand
deck.move_cards(hand,2)

print hand
## deal hands
deck3=Deck()
print("dealing")
#deck3.deal_hands(4,7)
