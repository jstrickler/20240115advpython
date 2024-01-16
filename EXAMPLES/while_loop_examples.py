
print("Welcome to ticket sales\n")

total = 0

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # Skip rest of loop; start back at top
    elif raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop
    elif not raw_quantity.isdigit():
        print("numbers only!")
        continue

    quantity = int(raw_quantity)  # could validate via try/except
    print(f"sending {quantity} ticket(s)")
    total += quantity

print(f"{total} tickets sold")