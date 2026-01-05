null_dict={}
null_dict['name']="college"
print(null_dict)

student={'name':'john',
         "subjects":{
                'maths':80,
                'science':90,
                'english':85
            },
         }
print(student)
print(student['subjects'])
#dictionary methods
print(student.keys())
print(list(student.keys())[1])
print(student.values())
print(student.items())
print(student.get('name')) # returns none if key not found
print(student.get('age','not found')) # returns default value if key not found 
student.update({'age':25})
print(student)
#Sets
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))
print(len(my_set)) #sets are mutable but elements are immutable .add tuple but not list or dictionary
my_set.add(6)
set1=set()
set1.add(10)
set1.remove(10)
print(set1)
set1.clear()
print(set1)
print(my_set.pop())
print(my_set.union({7,8,9}))
print(my_set.intersection({4,5,6,7}))
# table , cat 
d={'cat':"meow","table":["wood","glass"]}
print(d)
#one classroom for one subject. how many classrooms are needed 
subjects={"c++","java","python","html","css","javascript","python","html","java","c++"}
print(len(subjects))
#directly user update dictionary
student2={}
student2.update({"name":input("enter name:")})
student2.update({"age":int(input("enter age:"))})
student2.update({"marks":int(input("enter marks:"))})
print(student2)
#store 9,9.0,'9' in a set
set2={9,9.0,'9'}
print(set2)
values={("float",9.0),("int",9),("string",'9')}
print(values)