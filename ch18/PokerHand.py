from Card import *


class PokerHand(Hand): # inherits Hand class from card.py Hand inh from Deck

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards: # self.cards of hand which is [] initilally					#then new cards added bu movecards
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
	
    def rank_hist(self):
	self.ranks={}  #for ranks
	for card in self.cards:  # get cards from its objects
            
	    self.ranks[card.rank]=self.ranks.get(card.rank,0)+1	  
	
    def has_pair(self):
	self.rank_hist()
	for rank,count in self.ranks.items():
            if count >1:
               return True
        return False
    def has_twopair(self):
	self.rank_hist()
	pair_count =0
	for count in self.ranks.values():
	    if pair_count>1:
		return True
	    if count>1 :
		pair_count+=1
	return False
    def has_three_of_a_kind(self):
	self.suit_hist()
	for val in self.suits.values():
	    if val==3:
		return True
	return False    
 
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

if __name__ == '__main__':
    # make a deck
    deck = Deck()   # created some 4 suits with 13 ranks in it 
    deck.shuffle()  # shuflled suit rank list
    
    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand() # calling __init__ of hand class [] label=''
        deck.move_cards(hand, 7)  # has 7 -cards which is from deck
        hand.sort()		  # deck object super of hand and also PokerHand  				# sort memory location or realdata	
        print hand              # calls the Deck str method
	print ''		# self.cards its integrs encode analysis	
        print "Hand has flush", hand.has_flush()
        print "Hand has pair", hand.has_pair()
        print "Has has at least two pair", hand.has_twopair()
        print "Hand has 3 of a kind", hand.has_three_of_a_kind()
        print "#" * 40	
