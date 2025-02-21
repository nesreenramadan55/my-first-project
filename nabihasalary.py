import random

def manage_finances():
    salary = float(input("Enter your salary for the month: "))
    month = input("Enter the month: ")
    savings_percentage = float(input("Enter percentage for savings: "))
    rent_percentage = float(input("Enter percentage for rent: "))
    electricity_percentage = float(input("Enter percentage for electricity: "))
    
    savings_amount = (savings_percentage / 100) * salary
    rent_amount = (rent_percentage / 100) * salary
    electricity_amount = (electricity_percentage / 100) * salary
    
    total_expenses = savings_amount + rent_amount + electricity_amount
    remaining_salary = salary - total_expenses
    
    yearly_rent = rent_amount * 12
    yearly_electricity = electricity_amount * 12
    
    salary_squared = salary ** 2
    
    additional_savings = 50  
    savings_division = additional_savings / savings_amount if savings_amount != 0 else "N/A"
    

    print("\n===== Financial Summary for", month, "=====")
    print(f"Salary: ${salary:.2f}")
    print(f"Savings: ${savings_amount:.2f} ({savings_percentage}%)")
    print(f"Rent: ${rent_amount:.2f} ({rent_percentage}%)")
    print(f"Electricity: ${electricity_amount:.2f} ({electricity_percentage}%)")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Salary: ${remaining_salary:.2f}")
    print(f"Yearly Rent Estimate: ${yearly_rent:.2f}")
    print(f"Yearly Electricity Estimate: ${yearly_electricity:.2f}")
    print(f"Salary Squared (just for fun): {salary_squared:.2f}")
    print(f"Additional $50 savings divided by total savings: {savings_division}")
    print("====================================\n")

# Run the function
manage_finances()
