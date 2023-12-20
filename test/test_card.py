import pytest
from deck import Deck
from hand_players import Hand_Players
from card import Card

deck = Deck()

def test_check_valid_card():
    card_instance = Card(Hand_Players(deck), deck)

    card1 = (3, deck.clr1)
    card2 = (6, deck.clr2)
    card3 = (5, deck.clr1)
    card4 = (10, deck.clr3)

    assert card_instance.check_valid_card(card1, (4, deck.clr1)) == True
    assert card_instance.check_valid_card(card2, (4, deck.clr1)) == False
    assert card_instance.check_valid_card(card3, (4, deck.clr1)) == True
    assert card_instance.check_valid_card(card4, (4, deck.clr1)) == False

    assert card_instance.check_valid_card(card1, (8, deck.clr2)) == False
    assert card_instance.check_valid_card(card2, (8, deck.clr2)) == True
    assert card_instance.check_valid_card(card3, (8, deck.clr2)) == False
    assert card_instance.check_valid_card(card4, (8, deck.clr2)) == True

    assert card_instance.check_valid_card(card1, (3, deck.clr3)) == False
    assert card_instance.check_valid_card(card2, (3, deck.clr3)) == True
    assert card_instance.check_valid_card(card3, (3, deck.clr3)) == False
    assert card_instance.check_valid_card(card4, (3, deck.clr3)) == True


@pytest.fixture
def card_instance():
    return Card(Hand_Players(deck), deck)


def test_play_card(card_instance):
    player1_hand = [(3, deck.clr1), (5, deck.clr1), (7, deck.clr2)]
    player2_hand = [(6, deck.clr2), (10, deck.clr3), (2, deck.clr1)]

    card_instance.hand.player1_hand = player1_hand
    card_instance.hand.player2_hand = player2_hand

    table_card = (4, deck.clr1)

    card_instance.play_card(player1_hand, table_card)
    assert card_instance.true_card_p1 == [(3, deck.clr1), (5, deck.clr1)]

    card_instance.play_card(player2_hand, table_card)
    assert card_instance.true_card_p2 == []

