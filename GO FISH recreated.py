import random
suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "King", "Queen"]
deck = [(card, category) for category in suites for card in values]
deck_count = 48
player_hand = []
bot_hand = []
player_book_count = 0
bot_book_count = 0


def get_card(amount, person, requested_card):
    global deck_count
    card = ""
    asking_card = requested_card
    if person == "player":
        for i in range(amount):
            card = deck[random.randint(0,len(deck)-1)]
            player_hand.append(card)
            deck_count -= 1
            deck.remove(card)
        if card == asking_card:
            return True


    else:
        for i in range(amount):
            card = deck[random.randint(0,len(deck)-1)]
            bot_hand.append(card)
            deck_count -= 1
            deck.remove(card)
        if card == asking_card:
            return True
       


def ask_for_card(card, person):
    success = False
    if person == "player":
        for cards in bot_hand:
            if card == cards[0]:
                player_hand.append(cards)
                bot_hand.remove(cards)
                success = True
        if success == True:
            print("You successfully obtained {asked_card} go again".format(asked_card = card))
            return True
        else:
            print("Bot does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for you")
            return get_card(1, "player", card)




    else:
        for cards in player_hand:
            if card == cards[0]:
                bot_hand.append(cards)
                player_hand.remove(cards)
                success = True
        if success == True:
            print("Bot successfully obtained {asked_card}".format(asked_card = card))
            return True
            previous_value_accepted = True
        else:
            print("Player does not have {asked_card}".format(asked_card = card))
            print("Drawing a card for bot")
            return get_card(1, "bot", card)
            previous_value_accepted = False
    success = False
       
hand = []
def cards_in_hand():
    global hand
    hand.clear()
    for card in player_hand:
        hand.append(card[0])


    return hand

previous_value = ""
previous_value_accepted = True
def pick_a_card():
    multiple = 0
    first_card = bot_hand[0]
    max_number_and_value = [1, first_card[0]]
    value = 0
    card = 0
    mini_list = 0
    global previous_value
    global previous_value_accepted
    for i in range(len(bot_hand)-1):
        for card in bot_hand:
            mini_list = bot_hand[i]
            if card[0] == mini_list[0]:
                multiple += 1
                value = mini_list[0]
        if multiple > int(max_number_and_value[0]):
            max_number_and_value[0] = multiple
            max_number_and_value[1] = mini_list[0]
          
        multiple = 0
    if (max_number_and_value[1] == previous_value) and (previous_value_accepted == False):
        while max_number_and_value[1] == previous_value:
            value = bot_hand[random.randint(0,len(bot_hand)-1)]
            max_number_and_value[1] = value[0]
    previous_value = max_number_and_value[1]
    return max_number_and_value[1]

def check_book_and_set(person):
    chosen_card = ""
    card_count = 0
    global player_book_count
    global bot_book_count
    if person == "player":
        for card_list in player_hand:
            chosen_card = card_list[0]
            for card in player_hand:
                if card[0] == chosen_card:
                    card_count += 1
            if card_count == 4:
                for card in player_hand:
                    if card[0] == chosen_card:
                        player_hand.remove(card)
                player_book_count += 1
                print("Player set a book, card type was {card_type}".format(card_type=chosen_card))
            card_count = 0
    else: 
        for card_list in bot_hand:
            chosen_card = card_list[0]
            for card in bot_hand:
                if card[0] == chosen_card:
                    card_count += 1
            if card_count == 4:
                for card in bot_hand:
                    if card[0] == chosen_card:
                        bot_hand.remove(card)
                bot_book_count += 1
                print("Bot set a book")
            card_count = 0
    print("Player number of books: " + str(player_book_count))
    print("Bot number of books: " + str(bot_book_count))
       

           
       
       
turn_player = ""
random_number = random.randint(0,1)
if random_number == 0:
    turn_player = "player"
else:
    turn_player = "bot"


get_card(7, "player", "")
get_card(7, "bot", "")
print("Your hand: " + str(player_hand))
print("Bots hand: " + str(bot_hand))


print("This is the deck after drawing" + str(deck))
print("Deck count is: " + str(deck_count))


while deck_count > 0:
    if turn_player == "player":
        check_book_and_set("player")
        print("It is your turn")
        hand = cards_in_hand()
        print("The cards in you hand " + str(hand))
        asking_card = input("What value of will you ask for from the bot: ")
        while asking_card.title() not in hand:
            print("Sorry, that card is not in your hand")
            asking_card = input("Pick another card: ")
        success = ask_for_card(asking_card, "player")
        if success == True:
            turn_player = "player"
        else:
            turn_player = "bot"
            check_book_and_set("player")

    else:
        check_book_and_set("bot")
        print("It is bots turn")
        asking_card = pick_a_card()
        print("Bot is asking for {card}".format(card=asking_card))
        success = ask_for_card(asking_card, "bot")
        if success == True:
            turn_player = "bot"
        else:
            turn_player = "player"
            check_book_and_set("bot")

if player_book_count > bot_book_count:
    print("Player wins \nPlayer book count: {count} \nBot book count: {count2}\nPlayers hand is {players_hand}\nBots hand is {bots_hand}".format(count = player_book_count, count2 = bot_book_count, players_hand=player_hand, bots_hand=bot_hand))
elif player_book_count < bot_book_count:
    print("Bot Wins \nBot book count: {count} \nPlayer book count: {count2}\nPlayers hand is {players_hand}\nBots hand is {bots_hand}".format(count = bot_book_count, count2 = player_book_count, players_hand=player_hand, bots_hand=bot_hand))
else:
    print("Both parties have tied \nPlayer book count: {count} \nBot book count: {count2}\nPlayers hand is {players_hand}\nBots hand is {bots_hand}".format(count = player_book_count, count2 = bot_book_count, players_hand=player_hand, bots_hand=bot_hand))







   




print("Your hand: " + str(player_hand))
print("Bots hand: " + str(bot_hand))
