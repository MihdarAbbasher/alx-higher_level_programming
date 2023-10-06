#!/usr/bin/python3

li = [1, 2, 3, 4]
def fun(x):
    return x**2
    
l = list(map(fun, li))

print(l)    

l = list(map(lambda x: x**3, li))
print(l)    

