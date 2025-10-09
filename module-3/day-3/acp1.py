def change_return():
    total = float(input("Enter total bill amount: "))
    paid = float(input("Enter amount paid: "))
    if paid < total:
        print("Paid amount is less than total")
        return
    change = paid - total
    print("Shopkeeper should return:", round(change, 2), "$")

change_return()
