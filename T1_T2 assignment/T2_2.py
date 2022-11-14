x =int(input("enter the x value: "))
y = int(input("enter the y value:"))
operator = input("select the operator ADD,SUB, DIV, MUL, AVG: ")

while True:
    if operator == "ADD":
        result = x+y
        print("Addition of x and y:", result)
    elif operator == "SUB":
        result = x-y
        print("Subtraction of x and y: ", result)
    elif operator == "MUL":
        result = x*y
        print("Multiply x and y: ", result) 
    elif operator == "DIV":
        result = x/y
        print("Division of x and y: ", result)
    elif operator == "AVG":
        result = (x+y)/2
        print("Average of x and y: ", result)
    else:
        if result <0:
           print("result is negative")
