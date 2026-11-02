principal_amount_in_rupees = int(input("Enter first number"))
rate_of_interest_in_percent = float(input("Enter second number"))
time_in_years = int(input("Enter year"))
total_amount_in_rupees = principal_amount_in_rupees * (1 + rate_of_interest_in_percent / 100) ** time_in_years
compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees
print(f"total_amount_in_rupees={total_amount_in_rupees}")
print(f"compound_interest_in_rupees={compound_interest_in_rupees}")