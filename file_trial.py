import sys
f = sys.argv[1:]
print(f)
fp = open(f, 'r')
while True:
    text = fp.readline()
    print(text)
fp.close()
