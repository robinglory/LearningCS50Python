def main():
    camelCase = input("camel: ")
    snake_case= convert_snake(camelCase)
    print(snake_case)

def convert_snake(name):
    snake_case = ""

    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
        
    return snake_case

main()