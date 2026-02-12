

from app.operations import addition, subtraction, multiplication, division_positive, division_negative


def test_addition():
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(1,1) == 0

def test_multiplication():
    assert multiplication(2,3) == 6

def test_division_positive():
    assert division_positive(6,3) == 2 

def test_division_negative():
    assert division_negative(6,3) == -2

