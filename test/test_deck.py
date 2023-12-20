import pytest
from deck import Deck

@pytest.fixture
def deck_for_two_players():
    deck = Deck()
    deck.num_players = 2
    deck.deal_cards_to_players()
    return deck

@pytest.fixture
def deck_for_three_players():
    deck = Deck()
    deck.num_players = 3
    deck.deal_cards_to_players()
    return deck

@pytest.fixture
def deck_for_four_players():
    deck = Deck()
    deck.num_players = 4
    deck.deal_cards_to_players()
    return deck

def test_deck_creation():
    deck = Deck()
    assert deck.num_players == 0
    assert len(deck.DECK) == 72
    assert len(deck.table_deck) == 1
    assert len(deck.player1_deck) == 0
    assert len(deck.player2_deck) == 0
    assert len(deck.player3_deck) == 0
    assert len(deck.player4_deck) == 0

def test_deal_cards_to_players(deck_for_two_players, deck_for_three_players, deck_for_four_players):
    assert len(deck_for_two_players.player1_deck) == 36
    assert len(deck_for_two_players.player2_deck) == 36

    assert len(deck_for_three_players.player1_deck) == 24
    assert len(deck_for_three_players.player2_deck) == 24
    assert len(deck_for_three_players.player3_deck) == 24

    assert len(deck_for_four_players.player1_deck) == 18
    assert len(deck_for_four_players.player2_deck) == 18
    assert len(deck_for_four_players.player3_deck) == 18
    assert len(deck_for_four_players.player4_deck) == 18
