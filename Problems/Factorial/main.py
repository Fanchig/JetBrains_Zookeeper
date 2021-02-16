n = int(input())

hundreds = n // 100
tens = n // 10
units = n % 10

counter = 0
result = 1

while counter < n:
    counter += 1
    result *= counter
print(result)
