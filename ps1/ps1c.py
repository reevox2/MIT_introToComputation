# initialize investment formula variables
salary = float(input('Enter your annual salary: '))
annual_salary = salary
total_cost = 1000000.00
semi_annual_raise = .075
portion_down_payment = total_cost * 0.25
r = 0.04

# initialize bisection search variables
pHigh = 10000
pLow = 0
pGuess = ((pHigh - pLow) // 2) + pLow
portion_saved = pGuess/10000

months = 0
epsilon = 0
current_savings = 0
savingsEpsilon = 100
steps = 0

print('Checking the months')

while True:
    while current_savings < portion_down_payment and months < 40:
        if months != 0 and months % 6 == 0:
            annual_salary *= (1.0 + semi_annual_raise)
        current_savings += (portion_saved * (annual_salary/12)
                            ) + ((current_savings*r)/12)
        months += 1
    steps += 1
    print(months)
    print(current_savings)
    print(portion_saved)
    if abs(months - 36) <= epsilon and abs(current_savings - portion_down_payment) < savingsEpsilon:
        print('Best Savings Rate:', portion_saved)
        print('Steps in Bisection Search:', steps)
        break
    elif pHigh == pLow:
        print('It is not possible to save for this downpayment in 3 years.')
        break
    elif months > 36:
        pLow = pGuess + 1
        pGuess = ((pHigh + pLow) // 2)
        portion_saved = pGuess/10000
        print('^Portion save is too low')
        print('New pLow', pLow, '\n Current pHigh', pHigh)
    elif months < 36 or (current_savings - portion_down_payment) > savingsEpsilon:
        pHigh = pGuess - 1
        pGuess = ((pHigh + pLow) // 2)
        portion_saved = pGuess/10000
        print('^Portion saved is too high')
    months = 0
    current_savings = 0
    annual_salary = salary
