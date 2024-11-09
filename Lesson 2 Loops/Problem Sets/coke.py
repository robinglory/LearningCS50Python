def main():
    cost = 50
    amount_due = cost

    while amount_due>0:
        coin = int(input("Insert Coin: "))

        if coin in [10, 25, 5]:
            amount_due = amount_due - coin
        
        if amount_due >= 0:
            print(f"Amount Due: {amount_due}")
        

    changed_amount = abs(amount_due)

    print(f"Change Owed: {changed_amount}")


main()