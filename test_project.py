import pytest
from project import calculate_tax, bonus_credit, join_book_club
def main():
    test_calculate_tax()
    test_bonus_credit()
    test_join_book_club()

def test_calculate_tax():
    assert calculate_tax(12.00) == 0.84
    assert calculate_tax(13.99) == 0.98
    assert calculate_tax(54.48) == 3.81

def test_bonus_credit():
    assert bonus_credit(12.00) == 0.00
    assert bonus_credit(59.99) == 5.00
    assert bonus_credit(72.99) == 5.00

def test_join_book_club():
    assert join_book_club("y") == 10.00
