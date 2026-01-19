class B:
    def showB(self):
        print("B")


class A:
    def showA(self):
        print("A")



    def showA(self):
        print("A from class B")

class C(B, A):
    pass


# Creating object of class C
c = C()

# Calling methods
c.showB()
c.showA()
