#To calculate discount for checkout above 1000 and display final amount
total_price = float(input("Enter the total price: "))

if total_price > 1000:
    discount = total_price * 0.05
    final_amount = total_price - discount
    print(f"Discount applied: {discount}")
    print(f"The final amount after discount is: {final_amount}")
else:
    final_amount = total_price
    print("No discount applied for purchases of 1000 or less.")
    print(f"The final amount is: {final_amount}")