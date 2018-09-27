print("Welcome to git hub")
print("I add this from the net")
squared = 7 ** 2
cubed = 2 ** 3
print(cubed)
print(squared)
def my_function():
    print("hello people")

def add_all(a,b,c):
    print(int(a) +int( b) + int(c))

my_function()    

add_all(
    input(),
    input(),
    input()
)
class student:
    name = ""
    age = ""
    hobby = ""
    def description(self):
        desc_str ="my name is %s i am %s years old my hobby is %s." % (self.name,self.age,self.hobby)
    
        return desc_str

 #enter values for student
student1 = student()
print("enter name:")
student1.name = input()
print("enter age: ")
student1.age = input()
print("enter hobby:")
student1.hobby = input()

student2 = student()
print("enter name:")
student2.name =input()
print("enter age:")
student2.age =input()
print("enter hobby:")
student2.hobby =input()

#lets test the code
print(student1.description())
print(student2.description())

