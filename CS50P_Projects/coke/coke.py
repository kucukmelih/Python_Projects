fee = int(50)

while fee > 0:
    print(f"Amount Due: {fee}")
    payment = int(input("Insert Coin: "))
    if payment in [5, 10, 25]:
        fee -= payment
    else: fee += 0
    if fee < 0:
        break

print(f"Change Owed: {-fee}")
