import random
def play_game():
    player_cards = []
    computer_cards = []
    game_is_finished = False

    print("Welcome to Blackjack.")

    def draw_a_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = cards[random.randint(0, len(cards) - 1)]
        return card

    for i in range(2):                                                              # draw 2 cards at the start
        player_cards.append(draw_a_card())
        player_score = sum(player_cards)
        computer_cards.append(draw_a_card())
        computer_score = sum(computer_cards)

    print(f"Your cards are {player_cards}. Your current score is {player_score}.")  # Outputting the players cards
    if computer_cards[0] == 8 or computer_cards[0] == 11:                           # and the first computer card
        print(f"The computers first card is an {computer_cards[0]}.")
    else:
        print(f"The computers first card is a {computer_cards[0]}.")

    if player_score == 21 and len(player_cards) == 2:                               # Testing for a BlackJack
        print("You have a BlackJack, you win.")                                     # (sum(first 2 cards == 21))
        game_is_finished = True
    elif computer_score == 21 and len(player_cards) == 2:
        print("Computer has a BlackJack, Computer wins.")
        game_is_finished = True


    while game_is_finished is False:
        ask_draw = input("Do you want to draw another card? Type 'yes' or 'no'. ").lower()
        if ask_draw == "no" or ask_draw == "n":                                    # Asking if player wants another card
            while computer_score < 17:                                             # Computer needs to draw another card
                computer_cards.append(draw_a_card())                               # if the score is below 17
                computer_score = sum(computer_cards)
            print(f"The computers cards are {computer_cards} with a score of {computer_score}.")
            if player_score > computer_score:                                      # Comparing scores
                print("Your score is higher. You win.")
            elif player_score == computer_score:
                print("It's a draw.")
            elif player_score < computer_score <= 21:
                print("Your score is lower. Computer wins.")
            else:
                print("You win.")
            game_is_finished = True
        if ask_draw == 'yes' or ask_draw == 'y':                                  # Draw another card if player wants to
            player_cards.append(draw_a_card())
            player_score = sum(player_cards)
            print(f"Your cards are {player_cards}. Your current score is {player_score}.")
            if player_score > 21:
                print("Bad luck. Computer wins.")
                game_is_finished = True
    ask_again = input("Do you want to play again? Press 'yes' or 'no'. ").lower()   # Asking for another game
    if ask_again == "yes" or ask_again == "y":
        print("\n" * 100)
        play_game()
    else:
        print("bye")

def ask_play():                                                                     # Asking for a game at the start
    play_blackjack = input("Do you want to play a game of BlackJack? Press 'yes' or 'no'. ").lower()
    if play_blackjack == "no" or play_blackjack == 'n':
        print("bye")
    elif play_blackjack == "yes" or play_blackjack == 'y':
        play_game()
    else:
        print("Error")
        ask_play()

ask_play()
