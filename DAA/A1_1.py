# Program to display the Fibonacci series up to n-th term without recursion

print("Program to display the Fibonacci series up to n-th term without recursion")
nterms = int(input("Enter number of terms : "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
    
elif nterms == 1:
    print("Fibonacci series upto", nterms, ":")
    print(n1)
    
else:
    print("Fibonacci series:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
       # update values
        n1 = n2
        n2 = nth
        count += 1
