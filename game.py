from deck import Deck
from hand_players import Hand_Players
from card import Card
from rules import rules
import random
import keyboard
from tabulate import tabulate
from itertools import zip_longest
import time
#from control import Control

gameState = "Главное меню"

current_player = None
saved_time = 0
last_choice_time = time.time()

def choose_random_player():
    return random.randint(1, deck.num_players)

def switch_player():
    global current_player
    current_player = (current_player % deck.num_players) + 1
    print('Ходит игрок:', current_player)


def game():
    global deck, hand, card
    global num_players

    num_players = input("Введите количество игроков (2-4): ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            print("Количество игроков выбрано:", num_players)
        else:
            print("Неверное количество игроков. Попробуйте еще раз.")
            game()
    else:
        print("Неверный ввод. Попробуйте еще раз.")
        game()

    if 2 <= num_players <= 4:
        global gameState, last_choice_time
        gameState = 'Игра началась'
        if num_players == 2:
            deck = Deck()
            deck.num_players = num_players
            deck.deal_cards_to_players()

            hand = Hand_Players(deck)
            card = Card(hand, deck)

            hand.deal_cards_hand()
            print(tabulate(zip_longest(hand.player1_table, hand.player2_table, fillvalue=['', '']),
                           headers=['Рука 1 игрока', 'Рука 2 игрока'], tablefmt='grid'))

            valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
            valid_card2 = card.play_card(hand.player2_hand, deck.table_card)

            print("Центральная карта:", deck.table_card)
            print('Игрок 1 выбрал карту:', hand.player1_hand[0])
            print('Игрок 2 выбрал карту:', hand.player2_hand[0])

            if (len(card.true_card_p1) == 0 and len(card.true_card_p2) == 0
                    and len(deck.player1_deck) == 0 and len(deck.player2_deck) == 0):
                deck.table_card = deck.table_deck[-1]

                valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
                valid_card2 = card.play_card(hand.player2_hand, deck.table_card)

        if num_players == 3:
            deck = Deck()
            deck.num_players = num_players
            deck.deal_cards_to_players()

            hand = Hand_Players(deck)
            card = Card(hand, deck)

            hand.deal_cards_hand()
            print(tabulate(zip_longest(hand.player1_table, hand.player2_table, hand.player3_table, fillvalue=['', '']),
                           headers=['Рука 1 игрока', 'Рука 2 игрока', 'Рука 3 игрока'], tablefmt='grid'))

            valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
            valid_card2 = card.play_card(hand.player2_hand, deck.table_card)
            valid_card3 = card.play_card(hand.player3_hand, deck.table_card)

            print("Центральная карта:", deck.table_card)
            print('Игрок 1 выбрал карту:', hand.player1_hand[0])
            print('Игрок 2 выбрал карту:', hand.player2_hand[0])
            print('Игрок 3 выбрал карту:', hand.player3_hand[0])

            if (len(card.true_card_p1) == 0 and len(card.true_card_p2) == 0 and len(card.true_card_p3) == 0
                    and len(deck.player1_deck) == 0 and len(deck.player2_deck) == 0 and len(deck.player3_deck) == 0):
                deck.table_card = deck.table_deck[-1]

                valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
                valid_card2 = card.play_card(hand.player2_hand, deck.table_card)
                valid_card3 = card.play_card(hand.player3_hand, deck.table_card)

        if num_players == 4:
            deck = Deck()
            deck.num_players = num_players
            deck.deal_cards_to_players()

            hand = Hand_Players(deck)
            card = Card(hand, deck)

            hand.deal_cards_hand()
            print(tabulate(zip_longest(hand.player1_table, hand.player2_table, hand.player3_table, hand.player4_table,
                                       fillvalue=['', '']),
                           headers=['Рука 1 игрока', 'Рука 2 игрока', 'Рука 3 игрока', 'Рука 4 игрока'],
                           tablefmt='grid'))

            valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
            valid_card2 = card.play_card(hand.player2_hand, deck.table_card)
            valid_card3 = card.play_card(hand.player3_hand, deck.table_card)
            valid_card4 = card.play_card(hand.player4_hand, deck.table_card)

            print("Центральная карта:", deck.table_card)
            print('Игрок 1 выбрал карту:', hand.player1_hand[0])
            print('Игрок 2 выбрал карту:', hand.player2_hand[0])
            print('Игрок 3 выбрал карту:', hand.player3_hand[0])
            print('Игрок 4 выбрал карту:', hand.player4_hand[0])

            if (len(card.true_card_p1) == 0 and len(card.true_card_p2) == 0 and len(card.true_card_p3) == 0 and len(card.true_card_p4) == 0
                    and len(deck.player1_deck) == 0 and len(deck.player2_deck) == 0 and len(deck.player3_deck) and len(deck.player4_deck) == 0):
                deck.table_card = deck.table_deck[-1]

                valid_card1 = card.play_card(hand.player1_hand, deck.table_card)
                valid_card2 = card.play_card(hand.player2_hand, deck.table_card)
                valid_card3 = card.play_card(hand.player3_hand, deck.table_card)
                valid_card4 = card.play_card(hand.player4_hand, deck.table_card)

        keyboard.wait()


def menu():
    print("Меню:")
    print("1. Играть")
    print("2. Правила")
    print("3. Выход")


def main_menu():
    global gameState
    menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        game()
    elif choice == "2":
        rules()
    elif choice == "3":
        print("Выход из игры")
    else:
        print("Неправильный выбор, попробуйте еще раз.")


if gameState == 'Главное меню':
    main_menu()
