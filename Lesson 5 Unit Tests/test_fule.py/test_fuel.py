from fuel import convert,guage
import pytest

def main():
    test_convert()
    test_guage()

def test_convert():
    assert convert(1,2) == 50
    assert convert(1,4) == 25

def test_guage():
    assert guage(30) == "30%"
    assert guage(1) == "E"
    assert guage(99) == "F"

if __name__ == "__main__":
    main()