from functools import reduce


list =[1,2,3,4,5,6,7,8]

result = reduce(lambda a,d:10*a+d, [1,2,3,4,5,6,7,8],0)
print(result)
