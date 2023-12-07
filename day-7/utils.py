from enum import IntEnum

class Hand (IntEnum):
    HIGH_CARD = 1
    SINGLE_PAIR = 2
    DOUBLE_PAIR = 3
    THREE_OF_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_KIND = 6
    FIVE_OF_KIND = 7

CARD_ORDER: str = "23456789TJQKA"

def getHand(cards: str) -> Hand:
    count_of_diff_cards = sorted(list(map(cards.count, set(cards))))
    
    if len(count_of_diff_cards) == 1:
        return Hand.FIVE_OF_KIND
    
    if len(count_of_diff_cards) == 2: # either four of kind, or full house
        if count_of_diff_cards == [1,4]:
            return Hand.FOUR_OF_KIND
        else:
            return Hand.FULL_HOUSE
    
    if len(count_of_diff_cards) == 3: #either double pair, or three of a kind
        if count_of_diff_cards == [1,2,2]:
            return Hand.DOUBLE_PAIR
        else:
            return Hand.THREE_OF_KIND
            
    if len(count_of_diff_cards) == 4: 
        return Hand.SINGLE_PAIR

    return Hand.HIGH_CARD

def getJokeredHand(cards: str) -> Hand:
    return Hand.HIGH_CARD

def compareSameStrengthHand(hand1: str, hand2: str):
    assert len(hand1) == len(hand2)
    for i in range(len(hand1)):
        if hand1[i] != hand2[i]:
            return (CARD_ORDER.find(hand1[i]) - CARD_ORDER.find(hand2[i]))
        
    return 0

def hand_combination_sort(t1: tuple, t2: tuple):
    hand1 = getHand(t1[0])
    hand2 = getHand(t2[0])
    if hand1 == hand2: 
        return compareSameStrengthHand(t1[0], t2[0])
    else:
        return hand1 - hand2
