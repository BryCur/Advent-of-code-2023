from utils import *

totalValue = 0

cardCopies: dict = {}

with open("day-4/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        winning = getWinningNumber(line)
        checking = getPlayingNumber(line)

        intersection_count = len(getListIntersection(winning, checking))
        cardId = getCardId(line)
        if intersection_count != 0:
            # totalValue += pow(2, len(intersection_count) -1)

            currentCardCopy = cardCopies[cardId] if cardId in cardCopies else 1

            for key in range(cardId, cardId + intersection_count+1):
                if key in cardCopies and key == cardId:
                    cardCopies[key] += 1
                elif key in cardCopies:
                    cardCopies[key] += cardCopies[cardId]
                else: 
                    cardCopies[key] = cardCopies[cardId] if cardId in cardCopies else 1
        elif cardId in cardCopies:
            cardCopies[cardId] +=1
        else:
            cardCopies[cardId] =1
            


print(cardCopies)
print(sum(cardCopies.values()))
