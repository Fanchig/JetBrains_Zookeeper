user_input = int(input())

even_numbers = 2

while even_numbers < user_input:
    if 1 < user_input < 200:
        print(even_numbers)
        even_numbers += 2
    else:
        break