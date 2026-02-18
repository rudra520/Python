# Inputs
sales_amount = float(input("Enter total sales (USD): "))
discount_rate = 0.10  # 10% discount
exchange_rate = 0.92  # 1 USD to EUR

# Calculations_logic
discounted_price = sales_amount * (1 - discount_rate)
total_in_eur = discounted_price * exchange_rate

# Output
print(f"Final Price after discount: ${discounted_price:.2f}")
print(f"Total in EUR: €{total_in_eur:.2f}")