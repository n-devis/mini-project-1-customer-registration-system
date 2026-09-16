try:
    total_price = int(input("Enter total price: "))
    customers = int(input("Enter number of customers: "))

    average = total_price/customers
    print("Average:", average, "AED")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter numbers only.")