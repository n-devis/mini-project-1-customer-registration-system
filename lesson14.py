customer = {"name": "Davis", "service": "Basic cleaning", "price": 600, "status": "Confirmed" }
print(customer["name"])
print(customer["service"])
print(customer["price"])
print(customer["status"])
customer["service"] = "Office cleaning"
customer["price"] = 500
print(customer["service"])
print(customer["price"])
customer["phone"] = "0562342247"
print(customer["phone"])
for key, value in customer.items():
    print(key, ":", value)

customer1 = {"name": "Theo", "service": "Deep cleaning", "price": 500, "status": "pending"}
customer2 = {"name": "Royal", "service": "Glass cleaning", "price": 400, "status": "pending"}
customer3 = {"name": "Grace", "service": "Carpet cleaning", "price": 450, "status": "Confirmed"}
customers = [customer1, customer2, customer3]
for customer in customers:
    print("Customer:", customer["name"])
    print("Service:", customer["service"])
    print("Price:", customer["price"])
    print("Status:", customer["status"])
    if customer["status"] == "Confirmed":
        print("Booking is confirmed.")
    else:
        print("Booking is pending.")

