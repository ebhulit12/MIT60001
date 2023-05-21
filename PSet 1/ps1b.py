annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
semi_annual_raise = float(input("Enter the semi-annual raise (0-1): "))
total_cost = float(input("Enter the cost of your dream house: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04

months = 0

while(current_savings < portion_down_payment):
    monthly_salary = annual_salary / 12
    current_savings = current_savings + (current_savings * r / 12) + (
            portion_saved * monthly_salary)
    
    months += 1
    
    if (months % 6) == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    
print("Number of months: ", months)
    