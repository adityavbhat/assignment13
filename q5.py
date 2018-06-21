#1
try:
    print(time.ctime())
except :
    print("module not imported")

#2
try:
    x = int(input("Enter n"))
except ValueError:
    print("Enter Only Integer")

#3
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index out of range. Ramge = 0-2")
