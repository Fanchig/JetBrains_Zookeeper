initial_qty = int(input())  # 4
final_qty = int(input())  # 3

# half-life = time for an element to // 2 (E.g. 12 days for Radium)

half_life = 0

while initial_qty >= final_qty:
    initial_qty //= 2
    half_life += 1

half_life_in_days = half_life * 12
print(half_life_in_days)