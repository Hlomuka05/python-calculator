# Define the function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))  # Example input: 100
discount_percent = float(input("Enter the discount percentage: "))  # Example input: 25

# Call the function to calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price
if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
