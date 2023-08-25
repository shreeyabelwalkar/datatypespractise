elements=[10,20,30,40,50,60,206,253]
x=bytearray(elements)
print(x)
print(x[4])
x[0]=15
x[4]=55
print(x)

for i in x:
    print(i, end=' ')