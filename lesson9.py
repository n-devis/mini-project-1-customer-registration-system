total_spent = 400

if total_spent >= 2000:
    print("VIP customer")
elif total_spent >= 1000:
    print("Premium customer")
elif total_spent >= 500:
    print("Regular customer")
else:
    print("New customer")

service = input("Enter cleaning service.")

if service == "basic":
    print("Basic cleaning costs 150 AED.")
elif service == "deep":
    print("Deep cleaning costs 500 AED.")
elif service == "office":
    print("Office cleaning costs 800 AED.")
else:
    print("Service is not found.")

choice = input("How can we help you?")

if choice == "booking":
    print("Directing you to the bookings department.")
elif choice == "pricing":
    print("Our standard rates start from 150 AED.")
elif choice == "complaint":
    print("Connecting you with our manager.")
elif choice == "hours":
    print("We are open daily from 8 AM to 8 PM.")
else:
    print("Sorry, I don't understand that option.")

score = int(input("Enter employee performance score."))

if score >= 90:
    print("Performance: Excellent")
elif score >= 75:
    print("Performance: Very good")
elif score >= 60:
    print("Performance: Good")
else:
    print("Performance: Needs improvement")

