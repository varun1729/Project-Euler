import sys
file = open('54.txt', 'r')
P1 = []
P2 = []
for game in file:
	hand1 = []
	hand2 = []
	for x in range (0,30,3):
		if(x<15):
			card = [game[x] , game[x+1]]
			hand1.append(card)
		else:
			card = [game[x] , game[x+1]]
			hand2.append(card)
	P1.append(hand1)
	P2.append(hand2)

cardToValue = {'1' : 1,'2' : 2,'3' :3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13,'A':14}
valueToCard  = {cardToValue[k]: k   for k in cardToValue}
suits = ['H','C','S','D']

def getHighestValueCard (hand):
	maximum = 0
	for card in hand:
		val = cardToValue[card[0]]
		if (val > maximum):
			maximum = val 
	return maximum

def getHighCard (hand1, hand2):
	if (getHighestValueCard(hand1) > getHighestValueCard(hand2)):
		return 'P1'
	else:
		return 'P2'

#def checkRoyalFlush (hand):
	

P1Wins = 0
P2Wins = 0










		


