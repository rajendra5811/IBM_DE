count=1
while count<=5:
    print("Count is:",count)
    count+=1
#print 1to 100
count=1
while count<=100:
    print("Count is:",count)
    count+=1
    # print 100 to 1
count=100
while count>=1:
    print("Count is:",count)
    count-=1
  # print n th mulitiplication table
#n=int(input("enter a number:"))
n=5
count=1
while count<=10:
    print(n*count)
    count+=1
 # print [1,3,5,7,9]
mylist=[1,3,5,7,9]
i=0
while i<len(mylist):
    print(mylist[i])
    i+=1
# search an element in the list
mylist=[10,20,30,40,50]
#n=int(input("enter a number to search:"))
n=30
i=0
while i<len(mylist):
    if mylist[i]==n:
        print("element found at index:",i)
        break
    else:
        print("finding")
    i+=1
    
#continue statement
i=10
while i>=1:
    if(i%2==0):
        i-=1
        continue
    print(i)
    i-=1
# for loop not by indexing
mylist=[1,2,3,4,5]
for val in mylist:
    print(val)
tr="hello world"
for char in tr:
    if char=='l':
      print("letter l found")
      break
    print(char)
else:
    print("END OF LOOP") 
#print list elements using for loop [1,3,4,5,6]
s=[1,3,4,5,6,7,8,9]
for  val in s:
    if(val==6):
        print("6 found")
        break
    print(val)
    i=i+1
##print list elements using for loop ("1,3,4,5,6")
s=(1,3,4,5,6,7,8,9)
for r in s:
    if(r==6):
        print("6 found")
        break
    print(r)
    i=i+1
#range function start's from 0  1++
s=range(6)
print(s[5])
for i in s:
    print(i)
#range function with start , stop , step
s=range(1,11,4)
for i in s:
    print(i)
#print numbers from 1 to 100 using for loop and range function
for i in range(1,101):
    print(i)
#print num bers from 100 to 1 using for loop and range function
for i in range(100,0,-1):
    print(i)    
#print multiplication table of n using for loop and range function
n=7             
for i in range(1,11):
    print(n*i)
#Pass statement in for loop
for i in range(1,11):
    pass
#sum of first n natural numbers
n=10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Sum of first n numbers",sum)
# factorial of a number
n=5
fact=1
i=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial:",fact)
# factorial of a number using while loop    
n=5
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1    
print("Factorial:",fact)