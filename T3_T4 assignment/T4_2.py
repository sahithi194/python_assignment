str = "Welcom To Python Coding"
d ={"Upper Case":0,"Lower Case":0}

for c in str:
    if c.isupper():
        d["Upper Case"]+=1
    elif c.islower():
        d["Lower Case"]+=1
    else:
        pass
print("no.of upper case characters: ", d["Upper Case"])
print("no.of lower case characters: ",d["Lower Case"])

