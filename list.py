marks=[94.4, 88.7, 76.5, 92.3, 85.0]
print(marks)
print(type(marks))
print(len(marks))
student=["karan",95.4,17,"Delhi"]
print(student)
student[0]="Arun"
print(student)
#list methods
marks.append(89.5)
print(marks)
marks.insert(2,91.2)
print(marks)
marks.sort() #if list.sort() returns None and same with append() insert() 
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse() #marks=[85.0, 92.3, 76.5, 88.7, 94.4, 89.5, 91.2 ]
print(marks)
marks.remove(76.5)
print(marks)
marks.pop() #removes last element
print(marks)
#tuple
tp=(10,20,30,40,50)
print(tp)
#tuple methods
print(tp.count(20)) #1
print(tp.index(30)) #2
#wap to ask user to enter names of their 3 fav movies & store them in a list and print them
movies=[]
mov1=input("enter name of fav movie 1:")
mov2=input("enter name of fav movie 2:")   #movies.append(input("enter name of fav movie:")) 
mov3=input("enter name of fav movie 3:")
movies.append(mov1)
movies.append(mov2) 
movies.append(mov3)
print("your fav movies are:",movies)
#wap to check if a list is palindrome or not
lst=[1,2,3,2,1]
copy_lst=lst.copy()
copy_lst.reverse()
if lst==copy_lst:
    print("palindrome")
else:
    print("not palindrome")
#wap to count the number of students with A grade in a tuple
grades_tuple=('A','B','C','A','D','A','B')
grades_tuple.sort()
print(grades_tuple)
print("number of students with A grade:",grades_tuple.count('A'))