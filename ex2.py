a = 5
b = 5

if(a>b):
    print("A is greater than B")
elif (b>a):
    print("B is greater than A")
else:
    print("Seems like both are equal")

while (a < 10):
    print("I;m great")
    a = a + 1
#a = int(input())
#print(a)

for x in range(0, 9, 1):
    print("This is quite useful", x)

def addition (a, b):
    c = a + b
    return c
sum1  = addition(7,2)
print(sum1)

