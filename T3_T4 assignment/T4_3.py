list =[1,2,3,2,3,3,4,5]
unique_list =[]

for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

