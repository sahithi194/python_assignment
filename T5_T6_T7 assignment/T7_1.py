import math

numbers = input("Provide D: ")
numbers = numbers.split(',')
C =50
H=30
result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * C * int(D) / H))
    result_list.append(Q)

print(result_list)