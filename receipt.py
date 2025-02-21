def generate_receipt(name, date, items):
    print(f"name: \"{name}\"")
    print(f"date: \"{date}\"")
    print("\nlist of items\n")
    total_price = 0
    for item_name, price in items:
        print(f"{item_name:<10} ${price}")
        total_price += price
    print("\n" + "-"*20)
    print(f"total price   ${total_price}")