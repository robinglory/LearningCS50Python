from bank import value
import pytest

def main():
    testing_h()
    testing_Hello()
    testing_other()

from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20

def test_other():
    assert value("Yan Naing") == 100
    assert value("Good morning") == 100
    assert value("123") == 100

if __name__ == "__main__":
    main()

