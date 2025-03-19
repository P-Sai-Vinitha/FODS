def calculate_total(prices, quantities, discount_rate, tax_rate):
    subtotal = sum(p * q for p, q in zip(prices, quantities))  
    discount = subtotal * (discount_rate / 100)  
    total_after_discount = subtotal - discount  
    tax = total_after_discount * (tax_rate / 100)  
    total_cost = total_after_discount + tax  
    
    return total_cost

prices = [10, 20, 30]  
quantities = [2, 1, 3]  
discount_rate = 10  
tax_rate = 5  

total = calculate_total(prices, quantities, discount_rate, tax_rate)
print(f"Total Cost: ${total:.2f}")
