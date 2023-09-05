current_number = 3
sum_num = 0
index = 0
ratio = 0
print("The series is :")
while ratio < 47:
    print(current_number)
    sum_num = sum_num + current_number
    current_number += 4
    index += 1
    ratio = sum_num // index
print("The Sum of the numbers of the series is:", sum_num)
print("The Index of the ratio is:", index)
print("The ratio is:", ratio)
