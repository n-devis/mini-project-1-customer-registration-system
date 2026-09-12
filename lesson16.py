def welcome_customer(name):
    print(f"Welcome, {name}!")
welcome_customer("Theo")

def calculate_bill(price, quantity):
    total = price * quantity
    return total
basic_cleaning_bill = calculate_bill(500, 2)
print("Basic Cleaning:", basic_cleaning_bill)
deep_cleaning_bill = calculate_bill(400, 3)
print("Deep Cleaning:", deep_cleaning_bill)
office_cleaning_bill = calculate_bill(600, 1)
print("Office Cleaning:", office_cleaning_bill)

def checking_booking(status):
    if status == "Confirmed":
        return "Booking is confirmed"
    else:
        return "Booking is pending"
message = checking_booking("Confirmed")
print(message)
message = checking_booking("Not yet")
print(message)

customer = {"name": "Theo", "service": "Deep Cleaning", "price": 500, "status": "Confirmed"}
def show_customer(customer):
    print("Customer:", customer["name"])
    print("Service:", customer["service"])
    print("Price:", customer["price"])
    print("Status:", customer["status"])
show_customer(customer)

customers = [
    {"name": "Theo", "service": "Deep Cleaning", "price": 500, "status": "Confirmed"},
    {"name": "Hildah", "service": "Glass Cleaning", "price": 400, "status": "Confirmed"},
    {"name": "Davis", "service": "Floor Cleaning", "price": 600, "status": "Not paid"}]
def check_booking(status):
    if status == "Confirmed":
        return "Booking is confirmed"
    else:
        return "Booking is pending"

def process_customer(customer):
    print("Customer:", customer["name"])
    print("Service:", customer["service"])
    print("Price:", customer["price"])
    print("Status:", customer["status"])
    print("Status:", checking_booking(customer["status"]))
for customer in customers:
    process_customer(customer)

