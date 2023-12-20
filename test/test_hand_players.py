import pytest
from deck import Deck
from hand_players import Hand_Players

@pytest.fixture
def sample_deck():
    return Deck()

def test_take_card(sample_deck):
    hand_players = Hand_Players(sample_deck)

    assert len(hand_players.player1_hand) == 0
    hand_players.take_card(hand_players.player1_hand, [])
    assert len(hand_players.player1_hand) == 0

    assert len(hand_players.player2_hand) == 0
    hand_players.take_card(hand_players.player2_hand, [(3, 'green'), (5, 'blue'), (8, 'orange')])
    assert len(hand_players.player2_hand) == 1
    assert hand_players.player2_hand[0] == (3, 'green')

