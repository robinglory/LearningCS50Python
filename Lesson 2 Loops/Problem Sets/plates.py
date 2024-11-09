def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        is_length_valid(s) and
        starts_with_two_letters(s) and
        no_punctuation(s) and
        numbers_at_end(s)
    )


def is_length_valid(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[0:2].isalpha()


def no_punctuation(s):
    return s.isalnum()


def numbers_at_end(s):
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and i == 2:
                return False
            return s[i:].isdigit()
    return True

main()
