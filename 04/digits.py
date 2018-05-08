digits = []
for value in range(1, 10):
    digits.append(value)
digits.append(0)
print(digits)

min_digits = min(digits)
max_digits = max(digits)
sum_digits = sum(digits)

print(str(min_digits) + str(max_digits) + str(sum_digits))