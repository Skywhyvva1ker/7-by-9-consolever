import random


class Deck:
    num_players = 0
    def __init__(self):
        self.clr1 = 'green'  # +-1
        self.clr2 = 'blue'  # +-2
        self.clr3 = 'orange'  # +-3

        # достоинтсва карт
        self.NOMINALS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # поиск индекса по достоинству
        self.NAME_TO_VALUE = {n: i for i, n in enumerate(self.NOMINALS)}

        # карт в руке при раздаче на двух игроков
        self.CARDS_IN_HAND_MAX = 36

        # эталонная колода
        self.DECK = [(nom, color) for nom in self.NOMINALS for color in [self.clr1, self.clr2, self.clr3] for _ in range(2)]
        self.DECK.extend([(1, self.clr1), (2, self.clr1), (3, self.clr1), (4, self.clr1)])
        self.DECK.extend([(5, self.clr2), (6, self.clr2), (7, self.clr2), (8, self.clr2)])
        self.DECK.extend([(1, self.clr3), (2, self.clr3), (3, self.clr3), (9, self.clr3), (10, self.clr3)])

        # тасуем
        random.shuffle(self.DECK)

        # берем первую карту с колоды и кладем на стол
        self.table_card = self.DECK.pop()

        self.table_deck = [self.table_card]

        # делим на колоды
        self.player1_deck = []
        self.player2_deck = []
        self.player3_deck = []
        self.player4_deck = []

        self.num_cards_per_player = int


    def deal_cards_to_players(self):
        if self.num_players == 2:
            self.num_cards_per_player = 36
            self.player1_deck = self.DECK[:self.num_cards_per_player]
            self.player2_deck = self.DECK[self.num_cards_per_player:self.num_cards_per_player * 2]
        elif self.num_players == 3:
            self.num_cards_per_player = 24
            self.player1_deck = self.DECK[:self.num_cards_per_player]
            self.player2_deck = self.DECK[self.num_cards_per_player:self.num_cards_per_player * 2]
            self.player3_deck = self.DECK[self.num_cards_per_player * 2:self.num_cards_per_player * 3]
        elif self.num_players == 4:
            self.num_cards_per_player = 18
            self.player1_deck = self.DECK[:self.num_cards_per_player]
            self.player2_deck = self.DECK[self.num_cards_per_player:self.num_cards_per_player * 2]
            self.player3_deck = self.DECK[self.num_cards_per_player * 2:self.num_cards_per_player * 3]
            self.player4_deck = self.DECK[self.num_cards_per_player * 3:self.num_cards_per_player * 4]



