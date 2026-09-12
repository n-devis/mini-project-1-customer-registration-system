payment_received = False

if payment_received:
    print("Booking confirmed.") 
else:
    print("Booking pending.")

total_bill = 500

if total_bill >= 1000:
    print("Customer qualifies for a discount.")
else:
    print("Customer does not qualify for a discount.")


customer_name = input("Enter customer name: ")
booking_confirmed = input("Has the booking been confirmed? ")
if booking_confirmed == "yes":
    print("Booking confirmed for", customer_name)
else:
    print("Booking still pending for", customer_name)

job_cost = int(input("Enter the cleaning job cost (AED): "))
if job_cost > 500:
    print("Manager approval required.")
else:
    print("Job can proceed.")