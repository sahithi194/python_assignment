str = input("enter the string: ")
digits=0
letters=0
for i in str:
    if i.isdigit():
        digits =digits+1
    elif i.isalpha():
        letters =letters+1
    else:
        pass
print("letters: ", letters)
print("digits:",digits)
