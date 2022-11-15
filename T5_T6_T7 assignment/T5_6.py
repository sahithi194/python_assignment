#file_1 =open('doc.txt','w')
#file_1.write("Hello I am a file")
#file_1.write("\nWhere you need to return the data string")
#file_1.write("\nWhich is of even length")
#file_1.write("\nMake sure you return the content in The same link as it is present.")
file_2 = open('doc.txt','r')
for lines in file_2:
    words =lines.split()
    for word in words:
        if len(word)%2==0:
            print(word)
