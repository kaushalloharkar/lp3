# Program to display the Fibonacci series up to n-th term using recursion

print("Program to display the Fibonacci series up to n-th term with recursion")

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter number of terms : "))

print("Fibonacci series : ")
for i in range(n):
    print(fibonacci(i))
