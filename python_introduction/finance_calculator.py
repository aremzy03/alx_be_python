monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
rate = 0.05

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(annual_savings)}.")
