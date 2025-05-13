#students details

# blue print
# from tokenize import group


# class Student:
#   name = "uzma"
#   grade = 12

# # object - instance of class

# student1 = Student()
# print(student1.name, student1.grade)

# #problem is that its not giving dynamic value 
# #student2 = Student()
# #print(student2.name, student2.grade)


# class Student:
#   def __init__(self, full_name: str, class_grade: int, marks_obt: any, total_mrks: any, group:any):
#     self.name = full_name
#     self.grade = class_grade
#     self.marks = marks_obt
#     self.mrks = total_mrks
#     self.group = group

#   def student_details(self): #student detail method
#     print(f"{self.name} is in class {self.grade} from group {self.group}")

#   def percentage(self): #percentage method
#     percent = (self.marks * 100) / self.mrks
#     return f"{percent}%" 
  
# group1="pre-medical"
# group2="pre-eng"
  
# student1 = Student("uzma", 11, 400, 500, group1)
# print(student1.name, student1.grade)

# student2 = Student("imran", 10, 450, 500,group2)
# print(student2.name, student2.grade)

# student1.student_details() #becouse i use print in function
# student2.student_details()

# print(student1.percentage()) # here i use print becouse i use return in function
# print(student2.percentage())


#why we use self
# help karta hai class ki value access krny k lie  object main 
#or you can say
#object or class main relation banany main help karta hai
#we can use any other word but using self keyword is best approch


#print by using dict (key value pairs)

#print(student1.__dict__) 


# modify object property(if you want to add new value or delete)


# print(student1.name) # before modify
# student1.name = "yusra"
# print(student1.name) # after modify


# delete any object property

# print(student1.__dict__)
# del student1.grade
# print(student1.__dict__)

#delete object

# del student1
# print(student1)



#////////////////////////////////////second practice question///////////////////////////////////////
#code:

# class Teacher:

#     def __init__(self, teacher_name:str, teacher_subject:str,teacher_experience:int,teacher_salary:int):
#         self.name = teacher_name
#         self.subject = teacher_subject
#         self.experience = teacher_experience
#         self.salary = teacher_salary

#     def teacher_details(self):
#         print(f"name is {self.name} subject {self.subject} she has {self.experience} experience and her salary is {self.salary} and her yearly salary is {self.yearly_salary()} and she is {self.experience_level()}")    
    
#     def yearly_salary(self):
#         return self.salary*12
    
#     def experience_level(self):
#         if self.experience < 5:
#             return"junior teacher"
#         else:
#             return"senior teacher"


# Teacher1 = Teacher("ayesha","math", 2 ,20000)
# print(Teacher1.name)
# print(Teacher1.experience)
# Teacher1.teacher_details()
# print(Teacher1.yearly_salary())
# print(Teacher1.experience_level())


# Teacher2 = Teacher("marium","science", 5 ,25000)
# print(Teacher2.name)
# Teacher2.teacher_details()
# print(Teacher2.yearly_salary())
# print(Teacher2.experience_level())

# (//////////////////out put of this code///////////////////////////////
# ayesha
# 2
# name is ayesha subject math she has 2 experience and her salary is 20000 and her yearly salary is 240000 and she is junior teacher      
# 240000
# junior teacher
# marium
# name is marium subject science she has 5 experience and her salary is 25000 and her yearly salary is 300000 and she is senior teacher   
# 300000
# senior teacher
#/////////////////////////////////////////////////////////////////////// )



