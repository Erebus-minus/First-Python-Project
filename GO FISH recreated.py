import random 
suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen"]
deck = [(card, category) for category in suites for card in values]
deck_count = 48
player_hand = []
bot_hand = []

def get_card(amount, person):
    global deck_count
    if person == "player":
        for i in range(amount):
            player_hand.append(deck[random.randint(0,len(deck)-1)])
            deck_count -= 1
        else:
            for i in range(amount):
                bot_hand.append(deck[random.randint(0,len(deck)-1)])
                deck_count -= 1

def ask_for_card(card, person):
    success = False
    if person == "player":
        if card in bot_hand:
            for cards in bot_hand: 
                if card == cards[0]:
                    player_hand.append(card)
                    bot_hand.remove(card)
            print("You successfuly obtained {asked_card}".format(asked_card = card))
        else:
            print("Bot does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for you")
            get_card(1, "player")
            
    else:
        if card in player_hand:
            for cards in player_hand:
                if card == cards[0]:
                    bot_hand.append(card)
                    player_hand.remove(card)
        else:
            print("Player does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for you")
            get_card(1, "bot")
            

        
hand = []
def cards_in_hand(person):
    global hand
    hand.clear()
    if person == "player":
        for card in player_hand:
            hand.append(card[0])
    else:
        for card in bot_hand:
            hand.append(card[0])

    return hand


        
turn_player = ""
random_number = random.randint(0,1)
if random_number == 0:
    turn_player = "player"
else:
    turn_player = "bot"

get_card(7, "player")
get_card(7, "bot")
print(player_hand)
print(bot_hand)
if turn_player == "player":
    hand = cards_in_hand("player")
    print("The cards in you hand " + str(hand))
    asking_card = input("What value of will will you ask for from the bot: ")
    while asking_card.title() not in hand:
        print("Sorry, that card is not in your hand")
        asking_card = input("Pick another card: ")
    ask_for_card(asking_card, "player")
else:
    hand = cards_in_hand("player")
    print("The cards in you hand " + str(hand))
    asking_card = input("What value of will will you ask for from the bot: ")
    while asking_card.title() not in hand:
        print("Sorry, that card is not in your hand")
        asking_card = input("Pick another card: ")
    ask_for_card(asking_card, "player")

print(player_hand)
print(bot_hand)
    