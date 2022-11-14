import sys

file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)

if text:
    print(text[100])
