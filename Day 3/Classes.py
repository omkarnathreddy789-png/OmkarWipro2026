class student:
    name="Ohmkar"
    age=23
    
s1=student()
print(s1.name)
print(s1.age)

class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
e1=employee("Reddy",23)
print(e1.name,e1.age)
    
    