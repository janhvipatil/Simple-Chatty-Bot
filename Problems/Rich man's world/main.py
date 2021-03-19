initial_deposit = int(input())

year_count = 0

while initial_deposit <= 700000:
    initial_deposit += 0.071 * initial_deposit
    year_count += 1

print(year_count)
