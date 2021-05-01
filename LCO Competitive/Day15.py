percent_spent = 12
saving_percent = 100 - percent_spent

dollar_spent = 42

# print((350/100)*12)

deposit = 1
# Brute Force Solution
while True:
    if (((deposit/100)*percent_spent) == dollar_spent):
        break
    deposit += 1

print(f"Amount Deposited: ${deposit}")

deposit = (dollar_spent * 100) / percent_spent
print(f"Solution: Amount Deposited: ${deposit}")
