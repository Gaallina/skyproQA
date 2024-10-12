def bank(x, y):
    rate = 0.10
    sum_after_y_years = x * (1 + rate) ** y
    return sum_after_y_years


x = float(input("What amount would you like to deposit? "))
y = int(input("How many years would you like to keep your investment for? "))

result = bank(x, y)
print(f"If you deposit ${x} for {y} years then you will have ${result:.2f} on your account")
