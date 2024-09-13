import random
suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen"]
deck = [(card, category) for category in suites for card in values]
deck_count = 48
player_hand = []
bot_hand = []

def get_card(amount, person):
    global deck_count
    card = ""
    if person == "player":
        for i in range(amount):
            card = deck[random.randint(0,len(deck)-1)]
            player_hand.append(card)
            deck_count -= 10
            deck.remove(card)
    else:
        for i in range(amount):
            card = deck[random.randint(0,len(deck)-1)]
            bot_hand.append(card)
            deck_count -= 1
            deck.remove(card)

def ask_for_card(card, person):
    success = False
    if person == "player":
        for cards in bot_hand:
            if card == cards[0]:
                player_hand.append(cards)
                bot_hand.remove(cards)
                success = True
        if success == True:
            print("You successfuly obtained {asked_card}".format(asked_card = card))
        else:
            print("Bot does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for you")
            get_card(1, "player")

    else:
        for cards in player_hand:
            if card == cards[0]:
                bot_hand.append(cards)
                player_hand.remove(cards)
                success = True
        if success == True:
            print("Bot successfuly obtained {asked_card}".format(asked_card = card))
        else:
            print("Player does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for bot")
            get_card(1, "bot")
    success = False
       
hand = []
def cards_in_hand():
    global hand
    hand.clear()
    for card in player_hand:
        hand.append(card[0])

    return hand

def pick_a_card():
    multiple = 0
    max_number_and_value = [1, bot_hand[0]]
    card = 0
    mini_list = 0
    for i in range(len(bot_hand)-1):
        for card in bot_hand:
            mini_list = bot_hand[i]
            if card[0] == mini_list[0]:
                multiple += 1
        if multiple > int(max_number_and_value[0]):
            max_number_and_value = bot_hand[i]
            
        multiple = 0
    return max_number_and_value[1]
    
                
        
            
        
       
turn_player = ""
random_number = random.randint(0,1)
if random_number == 0:
    turn_player = "player"
else:
    turn_player = "bot"

get_card(7, "player")
get_card(7, "bot")
print("Your hand: " + str(player_hand))
print("Bots hand: " + str(bot_hand))

print("This is the deck after drawing" + str(deck))
if turn_player == "player":
    hand = cards_in_hand()
    print("The cards in you hand " + str(hand))
    asking_card = input("What value of will will you ask for from the bot: ")
    while asking_card.title() not in hand:
        print("Sorry, that card is not in your hand")
        asking_card = input("Pick another card: ")
    ask_for_card(asking_card, "player")
else:
    asking_card = pick_a_card()
    print("Bot is asking for {card}".format(card=asking_card))
    ask_for_card(asking_card, "bot")
    


print("Your hand: " + str(player_hand))
print("Bots hand: " + str(bot_hand))

