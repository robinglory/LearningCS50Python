from datetime import date, datetime
import inflect
import sys

def main():
    dob_str = input("Date of Birth: ")
    minutes = calculate_minutes(dob_str)
    if minutes is None:
        sys.exit("Invalid date")
    print(minutes)

def calculate_minutes(dob_str):
    try:
        birth_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        return None

    today = date.today()
    difference = today - birth_date
    total_minutes = round(difference.days * 24 * 60)

    p = inflect.engine()
    minutes_in_words = p.number_to_words(total_minutes, andword="").capitalize()
    return f"{minutes_in_words} minutes"

if __name__ == "__main__":
    main()
