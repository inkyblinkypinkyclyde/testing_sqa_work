import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Spades", 2)
    
    def test_card_has_suit(self):
        self.assertEqual("Spades", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(1, self.card1.value)
    
    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))
    
    def test_check_for_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))
    
    def test_check_for_card_total(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 3", CardGame.cards_total(self, cards))

    
