str="This is \tstring.\nNew line."
len1=len(str)
print(len1)
str1='lpucollege'
str2='''This is a sstring'''
final=str1 + " " + str2
print(final)
len2=len(final)
print(len2)
print(str1)
print(str2)
print(str)  
#"this is single line's comment" INDEXING can't assign new value in strings
print(str1[0]) #l
#slicing
print(str1[0:4]) #lpuc
print(str1[4:]) #college
print(str1[-3:-1]) #lpuco 
#string methods
str1="I am studying python from LPUCOLLEGE"
print(str1.capitalize()) #LPUCOLLEGE
print(str1.endswith("e")) #True
print(str1.count("l")) #2
print(str1.find("python")) #12
str1.replace("LPUCOLLEGE","LPU")
#practice
first_name=input("enter first name:")
print('length of first name:',len(first_name))
#WAP to find the occurence of '$' in the given string
str="hi, welcome $ to $ python $ programming"
print(str.count('$'))
#if else
age=21
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")
#if elif else
light="green"
if light=="red":
    print("stop")
elif light=="yellow":
    print("look")
elif light=="green":
    print("go")
else:
    print("invalid color")
#marks grading
marks=74
if marks>=90:
    print("grade A")    
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
else:
    print("grade D")
# nesting if else
age=34
if age>=18:
    if age<=60:
        print("eligible for work")
    else :
        print("senior citizen")
#wait to find largest number among three numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))     
c=int(input("enter third number:"))
if a>=b and a>=c:
    print("largest is:",a)              
elif  b>=c:
    print("largest is:",b)
else:
    print("largest is:",c)
#largest numberamong 4 numbers
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
n4=int(input("enter fourth number:"))
if n1>=n2 and n1>=n3 and n1>=n4:
    print("largest is:",n1)
elif n2>=n3 and n2>=n4:
    print("largest is:",n2)
elif n3>=n4:
    print("largest is:",n3)
else:
    print("largest is:",n4) 
#Wap to check if a number is a multiple of 7
num=int(input("enter a number:"))
if num%7==0:
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")