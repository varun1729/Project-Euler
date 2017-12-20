import sys
import time

t1 = time.monotonic()
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

def highCard (hand):
	maxCard = hand[0]
	for x in range (1,5):
		if (cardToValue[hand[x][0]] > cardToValue[maxCard[0]]):
			maxCard = hand[x] 
	return maxCard[0]

def royalFlush (hand):
	suite = hand[0][1]
	neededCards = ['T','J','Q','K','A']
	taken = []
	for card in hand:
		if (card[1] == suite):
			if ((card[0] in neededCards) and (card[0] not in taken)):
				taken.append(card[0])
			else:
				return (False, -1)
		else:
			return (False, -1)
	return (True, 0)

def straightFlush (hand):
	suite = hand[0][1]
	taken = []
	for card in hand:
		if (card[1] == suite):
			if (card[0] not in taken):
				taken.append(card[0])
			else:
				return (False, -1)
		else:
			return (False, -1)
	taken = sorted (cardToValue[taken[x]] for x in range (0,5)) 
	for x in range (0,4):
		if (taken[x]+1 != taken[x+1]):
			return (False, -1)
	return (True, taken[4])

def fourOfAKind (hand):
	values = sorted([hand[x][0] for x in range (0,5)])
	if ((values[0] == values[1]) and (values[0] == values[2]) and (values[0] == values[3])):
		return (True , cardToValue[values[3]])
	elif ((values[1] == values[2]) and (values[1] == values[3]) and (values[1] == values[4])):
		return (True, cardToValue[values [4]])
	return (False, -1)


def fullHouse (hand):
	values = sorted([hand[x][0] for x in range (0,5)])
	if ((values[0] == values[1]) and (values[0] == values[2]) and (values[3] == values[4])):
		return (True, cardToValue[values[2]])
	elif ((values[0] == values[1]) and (values[2] == values[3]) and (values[3] == values[4])):
		return (True, cardToValue[values[4]])
	return (False, -1)	

def flush (hand):
	if ((hand[0][1] == hand[1][1]) and (hand[0][1] == hand[2][1]) and (hand[0][1] == hand[3][1]) and (hand[0][1] == hand[4][1])):
		return (True, cardToValue[highCard(hand)]);
	return (False, -1);

def straight (hand):
	values = sorted([cardToValue[hand[x][0]] for x in range (0,5)])
	for x in range (0,4):
		if (values[x+1]-values[x] != 1):
			return (False, -1)
	return (True, values[4])

def threeOfAKind (hand):
	values = sorted([cardToValue[hand[x][0]] for x in range (0,5)])
	if ((values[0] == values[1]) and (values[0] == values[2])):
		return (True, values[2])
	elif ((values[1] == values[2]) and (values[1] == values[3])):
		return (True, values[3])
	elif ((values[2] == values[3]) and (values[2] == values[4])):
		return (True, values[4])
	return (False, -1)

def twoPairs (hand):
	hand = sorted(hand)
	pairCounter = 0
	temp = list()
	for x in range (0,5):
		counter = 0
		for y in range (x+1,5):
			if (hand[x][0]==hand[y][0]):
				counter+=1
		if (counter == 1):
			pairCounter+=1
			temp.append(cardToValue[hand[x][0]])
	if(pairCounter==2):
		temp = sorted(temp)
		return (True, temp[1])
	return (False, -1)


def onePair (hand):
	pairCounter = 0
	hand = sorted(hand)
	temp =[]
	for x in range (0,5):
		counter = 0
		for y in range (x+1,5):
			if (hand[x][0]==hand[y][0]):
				counter+=1
		if (counter == 1):
			pairCounter+=1
			temp.append(cardToValue[hand[x][0]])
	if(pairCounter==1):
		return (True, temp[0])
	return (False, -1)




temp = [['2', 'S'], ['3', 'H'], ['4', 'A'], ['K', 'H'], ['K', 'H']]

def evaluateHands (function, hand1, hand2):
	r1 = function(hand1)
	r2 = function(hand2)
	bool1 = r1[0]
	bool2 = r2[0]
	if ((bool1 == True) and (bool2 == True)):
		highCard1 = r1[1]
		highCard2 = r2[1]
		if (highCard1 == 0 and highCard2 ==0):
			#Royal Flush tieBreaker
			return 0.5
		elif (highCard1 > highCard2):
			return 1
		elif (highCard2 > highCard1):
			return 2
	elif ((bool1 == False) and (bool2 == False)):
		return 0
	elif (bool1 == True):
		return 1
	return 2

P1score = 0;
P2Score = 0;
booleanFunctions = [royalFlush, straightFlush, fourOfAKind, fullHouse, flush, straight, threeOfAKind, twoPairs, onePair]
for x in range (0,len(P1)):
	a = 0
	for function in booleanFunctions:
		a = evaluateHands (function, P1[x], P2[x])
		if (a == 1):
			P1score+=1
			break
		elif (a == 2):
			P2Score+=1
			break
		elif (a == 0.5):
			P1score += 0.5
			P2Score += 0.5
	if (a==0):
		highCard1 = cardToValue [highCard(P1[x])]
		highCard2 = cardToValue [highCard(P2[x])]
		if (highCard1 > highCard2):
			P1score+=1
		elif (highCard2>highCard1):
			P2Score+=1

t2 = time.monotonic()
print ("P1 Score:',P1score,'  P2 Score:", P2Score)
print ("Time taken: %.0fms" % ((t2-t1)*1000))



