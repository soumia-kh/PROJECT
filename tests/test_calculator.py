
# Test de multiplication
from app.calculator import multiplication

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(0, 5) == 0
    assert multiplication(-2, 3) == -6

# Test de addition
from app.calculator import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(0, 5) == 5
    assert addition(-2, 3) == 1