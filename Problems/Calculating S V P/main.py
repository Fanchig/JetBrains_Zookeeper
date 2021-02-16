# put your python code here
length = int(input())
width = int(input())
height = int(input())

sum_of_lengths = 4 * (length + width + height)
print(sum_of_lengths)

surface_area = 2 * (length * width + width * height + length * height)
print(surface_area)

volume = length * width * height
print(volume)