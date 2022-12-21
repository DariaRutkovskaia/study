import random


def deal_cards(players_cards):
    players_cards.append(random.choice(cards))
    return players_cards


def calculate_score(players_cards):
    if len(players_cards) == 2 and 10 in players_cards and 11 in players_cards:
        return 0
    elif 11 in players_cards and sum(players_cards) > 21:
        players_cards.remove(11)
        players_cards.append(1)
    return sum(players_cards)


def compare(score_p, score_c, ):
    if score_p == score_c:
        print(" It's a draw!")
    elif score_c == 0:
        print("You lose! Dealer has a Blackjack!")
    elif score_p == 0:
        print("You win! You have a Blackjack!")
    elif score_p > 21:
        print("You went over, you lose")
    elif score_c > 21:
        print("Computer loses")
    elif score_p > score_c:
        print("You win!")
    elif score_p < score_c:
        print("You lose")


def blackjack():
    users_cards = []
    computers_cards = []
    continue_game = True
    for i in range(2):
        deal_cards(users_cards)
        deal_cards(computers_cards)
    comp_first_card = computers_cards[0]
    users_score = calculate_score(users_cards)
    comp_score = calculate_score(computers_cards)
    print(f"Your cards: {users_cards}, current score: {users_score}")
    print(f"Computer's first card: {comp_first_card}")
    print('\n' * 2)
    if calculate_score(users_cards) == 0 or calculate_score(computers_cards) == 0:
        compare(users_score, comp_score)
    elif calculate_score(users_cards) > 21:
        compare(users_score, comp_score)
    else:
        while continue_game and input('Type "y" to get another card. Type "n" to pass ') == "y":
            deal_cards(users_cards)
            users_score = calculate_score(users_cards)
            print(f"Your cards: {users_cards}, current score: {users_score}")
            print(f"Computer's first card: {comp_first_card}")
            print('\n' * 2)
            if calculate_score(users_cards) == 0 or calculate_score(computers_cards) == 0:
                continue_game = False
            elif calculate_score(users_cards) > 21:
                continue_game = False

        else:
            while comp_score < 17:
                deal_cards(computers_cards)
                comp_score = calculate_score(computers_cards)
            compare(users_score, comp_score)
        print(f"Your final hand: {users_cards}, final score: {users_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {comp_score}")
    print('\n' * 2)
    if input('Do you want to play a game of BlackJack? Type "y" or "n" ') == "y":
        blackjack()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if input('Do you want to play a game of BlackJack? Type "y" or "n" ') == "y":
    from art import logo

    print(logo)
    blackjack()
