#calculate penalty amount for returning book late
from datetime import datetime

# Get user inputs
book_code = input("Enter item code: ")
expected_return = input("Enter expected return date (dd/mm/yyyy): ")
actual_return = input("Enter actual return date (dd/mm/yyyy): ")

# Convert input dates to datetime objects
expected_return_date = datetime.strptime(expected_return, "%d/%m/%Y")
actual_return_date = datetime.strptime(actual_return, "%d/%m/%Y")

# Calculate days late
days_late = (actual_return_date - expected_return_date).days

# Determine penalty rate using if-else statement
if days_late <= 7:
    penalty_rate = 20
elif 8 <= days_late <= 14:
    penalty_rate = 50
else:
    penalty_rate = 100

# Calculate total penalty
total_penalty = days_late * penalty_rate

# Display results
print("Book Code:", book_code)
print("Expected Return Date:", expected_return_date.strftime("%d/%m/%Y"))
print("Actual Return Date:", actual_return_date.strftime("%d/%m/%Y"))
print("Days Late:", days_late)
print("Penalty Rate:", penalty_rate)
print("Total Penalty:", total_penalty)