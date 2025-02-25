def main():
    text = input("Input: ")
    result = shorten(text)
    print("Output:", result)

def shorten(text):
    vowels = "AEIOUaeiou"
    no_vowels_text = ""
    for char in text:
        if char not in vowels:
            no_vowels_text += char
    return no_vowels_text

if __name__ == "__main__":
    main()
