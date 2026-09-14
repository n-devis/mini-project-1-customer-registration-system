try:
    price = int(input("Enter cleaning service price: "))
    quantity = int(input("Enter number of bookings: "))

    total = price * quantity

    print("Total:", total, "AED")

except ValueError:
    print("Invalid input. Please enter numbers only.")