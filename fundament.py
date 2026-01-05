print('hello world')
name='shradha'
age=23
price=45.67
print('name:',name)
print('age:',age)
print('price:',price)
print(type(name))
print(type(age))                        
print(type(price))

name1='john'
name2="jhon"
name3='''jhon'''
print(name1)
print(name2)
print(name3)
age1=25
old=False
a=None
print(type(age1))
print(type(old))        
print(type(a))

a=2
b=5
sum=a+b
print('sum:',sum)
diff=b-a
print('difference:',diff)
#linecomment
"""this is multiline
comment """
#Operators arthimatic Relational Logical Assignment 
print(a+b) #7
print(b-a) #3
print(a*b) #10
print(b/a) #2.5
print(b%a) #1
print(a**b) #32
#Relational
print(a==b) #False
print(a!=b) #True
print(a>b) #False
print(a<b) #False
print(a>=b) #False
print(a<=b) #True
#assignment
num=10
num+=5 #num=num+5
print(num) #15
num-=3 #num=num-3
print(num) #12
num*=2 #num=num*2
print(num) #24
num**=2 #num=num**2
print(num) #576
#logical
print(not(True)) #False
a=50
b=30
print(not(a>b)) #False
val1=True
val2=True
print("ans operator:", val1 and val2) #True
print("or operator:", val1 or val2) #True
print("or operator:", (a==b)or (a>b)) #True

#type conversion is automatic 
a=2
b=5.6
sum=a+b # 2.0+5.6=7.6
print('sum:',sum)
a="2"
b=5
#print("sum:",a+b) #sum=a+b #error 
c=int(a)# convert string to integer type casting
sum=c+b #2+5=7
print("sum :",sum)
#d=float("shradha") #error any data need match to convert to float
b=str(b) #5 to "5"
print(type(b))
#userinput function
name=input("enter your name:")
age=input("enter your age:")
marks=input("enter your marks:")
val=input("enter any value:")
 
print("welcome",name) 
print("age:",age)
print("marks:",marks)
print(type(val),val)
#Practice programs
#Write a Program to input 2 numbers and print their sum
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("sum:",num1+num2)
#WAP to input side of square and print its area
side=float(input("enter side of square:"))
print("area of square:",side**2)
#WAP to input 2 float numbers and print their average
a=float(input("enter first float number:"))
b=float(input("enter second float number:"))
print("average:",(a+b)/2)   
#WAP to input 2 numbers, a and b.Print a is greater than or equal to b. if not print False
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(a>=b)