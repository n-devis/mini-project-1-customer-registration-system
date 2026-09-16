try:
    name = input("Enter the customer's name: ")
    price = int(input("Enter the service price: "))
    bookings = int(input("Enter the number of bookings: "))

    if bookings == 0:
        print("Number of bookings cannot be zero.")
    else:
        total = price * bookings

        print()
        print("Customer:", name)
        print("Total bill:", total, "AED")

except ValueError:
    print("Invalid input. Please enter numbers only.")