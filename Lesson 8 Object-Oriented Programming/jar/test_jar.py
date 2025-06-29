import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)  # Negative capacity invalid

    with pytest.raises(ValueError):
        Jar("large")  # Non-integer capacity invalid

def test_str():
    jar = Jar(5)
    assert str(jar) == ""  # Empty jar

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2

    jar.deposit(3)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)  # Exceeds capacity

    with pytest.raises(ValueError):
        jar.deposit(-1)  # Negative deposit invalid

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)  # More than current size

    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Negative withdraw invalid
