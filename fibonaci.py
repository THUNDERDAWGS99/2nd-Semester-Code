#fibonaci 
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

#asks user for how many of fibonaci they want to see
x = int(input("How many numbers of the fibonaci do you want to see? "))

#prints Fibonaci numbers based on the input
print(" ")
print("Fibonaci sequence:")
print(" ")
for i in range(x):
    print(fib(i))
