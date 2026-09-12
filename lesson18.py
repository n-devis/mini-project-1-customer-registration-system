import json
customer = {"name": "Theo", "service": "Deep Cleaning", "price": 500, "status": "Confirmed"}
json_data = json.dumps(customer, indent=4)
print(json_data)

with open("customer.json", "w") as file:
    json.dump(customer, file, indent=4)
    print("Customer saved successfully")

json_data = '{"name": "Theo", "service": "Deep Cleaning", "price": 500, "status": "Confirmed"}'
customer = json.loads(json_data)
print(customer)
print(customer["name"])
print(customer["service"])



