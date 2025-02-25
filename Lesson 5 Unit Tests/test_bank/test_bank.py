from bank import value
import pytest

def main():
    testing_h()
    testing_Hello()
    testing_other()

def testing_Hello():
    assert value("Hello") == "$0"

def testing_h():
    assert value("hello") == "$20"

def testing_other():
    assert value("Yan Naing") == "$100"

if __name__ == "__main__":
    main()
