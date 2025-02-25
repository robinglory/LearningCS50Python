from twttr import shorten
import pytest
def main():
    testing()

def testing_str():
    assert shorten("twitter") == "twttr"
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50") == "CS50"
    assert shorten("aeiou") == ""

if __name__ == "__main__":
    main()