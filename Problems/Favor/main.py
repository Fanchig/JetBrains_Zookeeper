k = int(input())

counter = 0
total = 0

while counter < k:
    counter += 1
    total += counter
print(total)

# Short inline alternative:
# print(k * (k + 1) // 2)