# put your python code here

# Solution 1 ()

user_input = int(input())  # 476

hundreds = user_input // 100  # 4
tens = user_input % 100 // 10  # 7
units = (user_input % 100) % 10  # 6

print(hundreds + tens + units)  # Calculate sum of integers

# Solution 2 (indexes)
# user_input = input()
#
# user_input_int_0 = int(user_input[0])
# user_input_int_1 = int(user_input[1])
# user_input_int_2 = int(user_input[2])
#
# result = user_input_int_0 + user_input_int_1 + user_input_int_2
# print(result)