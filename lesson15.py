customer_name = "Theo"
service = "Deep Cleaning"
company = "My Cleaning Company"
message = f"{customer_name} booked {service} with {company}."
print(message)

service = " deep cleaning "
print(service.strip().lower())

customer = input("Enter your name:")
customer = customer.strip()
print(f"Welcome, {customer}!")

service = input("Enter cleaning service:")
service = service.strip().lower()
if service == "basic":
    print("Basic cleaning costs 150 AED")
elif service == "deep":
    print("Deep cleaning costs 500 AED")
elif service == "office":
    print("Office cleaning costs 800 AED")
else:
    print("Service not found")


message = input("Enter your message:")
message = message.lower()
if "deep" in message:
    print("Customer is asking about deep cleaning.")
elif "price" in message:
    print("Customer is asking about pricing.")
elif "booking" in message:
    print("Customer is asking about booking.")
elif "complaint" in message:
    print("Customer has a complaint.")
   
