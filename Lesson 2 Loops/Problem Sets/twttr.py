def main():
    text = input("Input: ")
    result = remove_vowels(text)
    print("Output:", result)

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    no_vowels_text = ""
    for char in text:
        if char not in vowels:
            no_vowels_text += char
    return no_vowels_text

main()
