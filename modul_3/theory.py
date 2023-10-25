#def print_max(a, b):
    #if a > b:
        #print(a, "max")
    #elif a == b:
        #print(a, "дорівнює", b)
    #else:
        #print(b, "max")
#a = 5
#b = 6
#print_max(a, b)
# OR
#print_max(5, 6)

# ОБЛАСТЬ ВИДИМОСТІ ЗМІННОЇ 
x = 50
def fun():
    x = 2
    print("change local value x on", x)
fun()
print("x як і раніше", x)

# GLOBAL
у = 10
def f():
    global y
    print("y =", y)
    y = 5
    print("Змінили глобальне значення у на", y)
f()
print("Значення у дорівнює", y)

# LAMBDA

print((lambda x, y: x + y)(6, 8))