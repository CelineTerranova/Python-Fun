import random

# DEFINE THE FUNCTION THAT WILL RETURN TRUE IF HAND 1 BEATS HAND 2 AND FALSE OTHERWISE.

def blackjack_hand_greater_than(hand_1, hand_2):

    dmin = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}
    dmax = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}

    val1min = 0
    val1max = 0
    val2min = 0
    val2max = 0

    for i in hand_1:
        val1min = val1min + dmin[i]
        val1max = val1max + dmax[i]

    for j in hand_2:
        val2min = val2min + dmin[j]
        val2max = val2max + dmax[j]
    #print('Val1min =', val1min, 'Val1max =', val1max, 'Val2min =', val2min, 'Val2max =', val2max)

    if val1max >21 : bestvalue1 = val1min
    else: bestvalue1 = val1max
    if val2max >21 : bestvalue2 = val2min
    else: bestvalue2 = val2max

    if bestvalue1 > 21: return False
    elif bestvalue2 > 21 : return True
    elif bestvalue1 > bestvalue2: return True
    else: return False


# DEFINE THE FUNCTION THAT WILL RETURN TRUE IF DEALER SHOULD HIT OR FALSE IF SHOULD STAND

def blackjack_hitorstand(hand):
    dmin = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}
    dmax = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}
    handmin = 0
    handmax = 0

    for i in hand:
        handmin = handmin + dmin[i]
        handmax = handmax + dmax[i]

    if handmax >= 17: return False
    else : return True


# DEFINE A FUNCTION THAT CALCULATE THE TOTAL FOR A HAND
def total_hand(hand):
    dmin = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}
    dmax = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 10, 'Q':10, 'K':10}
    valmin = 0
    valmax = 0
    total = 0
    for i in hand:
        valmin = valmin + dmin[i]
        valmax = valmax + dmax[i]

    if valmax >21 : total = valmin
    else: total = valmax
    return total


# INITIAL CARDS DISTRIBUTION

player = list()
dealer = list()
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

print("Dealing cards...")
player.append(random.choice(cards))
player.append(random.choice(cards))
print('Your hand so far: ', player)
dealer.append(random.choice(cards))
dealer.append(random.choice(cards))
print('Dealer\'s hand so far', dealer)


# INTERACTIVE GAME: PLAYER DECIDES TO HIT OR STAND

while True:
    i = input("Do you want another card? hit or stand: ")
    if (i == 'stand'): break
    if i != 'hit' and i != 'stand':
        print('Please choose a valid option: type \"hit\" or \"stand\"')
        continue
    player.append(random.choice(cards))
    print('Your hand so far: ', player)

    if (blackjack_hitorstand(dealer) is True):
        dealer.append(random.choice(cards))
    print('Dealer\'s hand so far', dealer)


#  DEALER DECIDES WHETHER TO GET MORE CARDS AFTER PLAYER STANDS
while blackjack_hitorstand(dealer) is True:
    dealer.append(random.choice(cards))


# CALCULATE AND PRINT THE WINNING HAND
print('Your final hand: ', player, 'and the total is: ', total_hand(player))
print('Dealer\'s final hand', dealer, 'and the total is: ', total_hand(dealer))
print('YOU WON!' if blackjack_hand_greater_than(player, dealer) is True else 'YOU LOST :(')
