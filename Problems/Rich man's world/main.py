initial_sum = int(input())
interest_rate = 7.1 / 100

years = 0
while initial_sum < 700000:
    initial_sum += initial_sum * interest_rate
    years += 1

print(years)