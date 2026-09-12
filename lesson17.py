with open("customers.txt", "w") as file:
    file.write("Theo\n")
    file.write("Sarah\n")
    file.write("Ahmed\n")
with open("customers.txt", "r") as file:
    print(file.read())

with open("customers.txt", "a") as file:
    file.write("Hildah\n")
with open("customers.txt", "r") as file:
    print(file.read())

customer_name = input("Enter customer name:").strip()
with open("customers.txt", "a") as file:
    file.write(customer_name + "\n")
    print("Customer saved successfully.")

customer = {"name": "Theo", "service": "Deep Cleaning", "price": 500, "status": "Confirmed"}
record = (f"Customer: {customer['name']}\n"
          f"Service: {customer['service']}\n"
          f"Price: {customer['price']} AED\n"
          f"Status: {customer['status']}")
with open("bookings.txt", "a") as file:
          file.write(record)
with open("bookings.txt", "r") as file:
          print(file.read())


