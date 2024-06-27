# Task 2: Bank Interest If you have a savings account with a particular initial amount 
# and a fixed yearly interest rate, calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700.

# Bank Interest

savings = 10000.00
interest_rate = 0.07

interest = savings * interest_rate
year_one = savings + interest

print(round(year_one))