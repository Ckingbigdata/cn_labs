'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = float(input("Enter an investment amount: " ))
rate = float(input("Enter a rate as a percentage: "))
period = float(input("Enter the number of years to invest: "))
FV = float(amount * (1 + rate)**period)
print(FV)
