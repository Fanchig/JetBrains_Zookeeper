# put your python code here
class_1 = abs(int(input()))
class_2 = abs(int(input()))
class_3 = abs(int(input()))

desks_class_1 = class_1 % 2 + class_1 // 2
desks_class_2 = class_2 % 2 + class_2 // 2
desks_class_3 = class_3 % 2 + class_3 // 2

total = desks_class_1 + desks_class_2 + desks_class_3

print(total)