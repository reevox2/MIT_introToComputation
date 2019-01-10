annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04

months = 0

while current_savings < portion_down_payment:
    if months != 0 and months % 6 == 0:
        annual_salary *= (1.0 + semi_annual_raise)
    current_savings += (portion_saved * (annual_salary/12)
                        ) + ((current_savings*r)/12)
    months += 1

print('Saved:', current_savings)
print('Number of months: ', months)
print('Human Readable: ', months//12, 'years and', months % 12, 'months.')
