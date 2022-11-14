#l1 = [1,2,3,4,5,6,7,8,9,10]
 
#eve_num = map(lambda x: x**2, filter(lambda  x: x%2==0, l1))
 
#print(eve_num)

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)
