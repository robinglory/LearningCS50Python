import sys
import random
import pyfiglet

def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        font = sys.argv[2]
    else:
        font = None

    figlet = pyfiglet.Figlet()

    if font:
        if font not in figlet.getFonts():
            sys.exit("Invalid usage")
        figlet.setFont(font=font)
    else:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)

    user_text = input("Input: ")

    print(figlet.renderText(user_text))

if __name__ == "__main__":
    main()
