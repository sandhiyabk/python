a=17
b=23
temp=a
a=b
b=temp
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
a,b=b,a
print(a)
print(b)
a=a ^ b
b=a ^ b
c=a ^ b #it's not work
print(a)
print(b)
