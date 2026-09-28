from datetime import datetime

now = datetime.now()

print(now)

from datetime import datetime

now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)





from datetime import datetime

now = datetime.now()

booking_date = now.strftime("%d-%m-%Y")
booking_time = now.strftime("%H:%M")

customer = "Theo"
service = "Deep Cleaning"
price = 500

print("Customer:", customer)
print("Service:", service)
print("Price:", price, "AED")
print("Booking date:", booking_date)
print("Booking time:", booking_time)