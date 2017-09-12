# User must input principal, Compound rate, annual rate, and years.
P = int(input("Enter starting principle please. "))
n = int(input("Enter Compound intrest rate.(daily, monthly, quarterly, half-year, yearly) "))
r = float(input("Enter annual interest amount. (decimal) "))
t = int(input("Enter the amount of years. "))

final = P * (((1 + (r/(100.0 * n))) ** (n*t)))

print(final)
