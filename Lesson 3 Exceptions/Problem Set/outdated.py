def main():
    while True:
        date = input("Date: ").strip()
        try:
            # Check for MM/DD/YYYY format
            if "/" in date:
                month, day, year = map(int, date.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            # Check for "Month Day, Year" format
            else:
                month_names = [
                    "January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"
                ]
                month_day, year = date.rsplit(",", 1)
                month_str, day = month_day.rsplit(" ", 1)
                month = month_names.index(month_str) + 1
                day = int(day.strip())
                year = int(year.strip())
                if 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            pass  # Prompt again if invalid

if __name__ == "__main__":
    main()
