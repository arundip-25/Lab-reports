num=int(input("Enter the number "))
a=0
b=1
print(a)
print(b)
for i in range(num):
    c=a+b
    a=b
    b=c
    print(c)