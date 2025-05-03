import re

def validate(ip):
    # Regular expression to match four numbers separated by dots
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    
    if not match:
        return False  # Doesn't match the basic pattern

    # Extract numbers and check if each is between 0 and 255
    numbers = [int(num) for num in match.groups()]
    
    return all(0 <= num <= 255 for num in numbers)
