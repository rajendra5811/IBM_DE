def sum(a,b):
    return a+b
print("Sum:",sum(3,5))

def avg(a,b,c):
    return (a+b+c)/3
print("Average:",avg(4,6,8))
print("Hello World",end="$") #ssep='
print("eshwar")#end ='/n' by default
"""(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None"""
"""(function) def len(
    obj: Sized,
    /
) -> int
Return the number of items in a container."""
"""(class) range
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement)."""
def multiply(x,y=1): # default parameters start from last(x=1,y) error
    print(multiply(2,3))
    return x*y
cities = ["bangalore","mumbai","chennai","delhi"]
heroes = ["ironman","thor","hulk","captain america"]

def print_len(list):
    print(len(list))

def print_list(list):
    for i in list:
        print(i,end=" ")


print_list(heroes) # % symbol is used for chain or use print.
print_len(cities)
#factorial function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("Factorial:",factorial(6))
#usd to inr conversion
def convert(usd):
    inr=usd*82.74
    print("INR:",inr)
convert(13)
#odd or even
def odd_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
odd_even(7)
#recursion function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
#factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
        print(n) 
print("Factorial using recursion:",fact(5))
# sum of n natural numbers using recursion
def sum_n(n):
    if(n==0):
        return 0
    else:
        return n+sum_n(n-1)
print(sum_n(10))
#print list elements using recursion
def print_list(al, i=0):
    if i >= len(al):
        return
    print(al[i])
    print_list(al, i + 1)
al = [1, 3, 4, 5, 6]
print_list(al)