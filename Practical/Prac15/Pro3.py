

class A:
    def parent(self):
        print("I am Parent class")


class B(A):
    def child(self):
        print("class B, I am child of class A")


class C(A):
    def child(self):
        print("class C, I am child of class A")


b = B()
b.parent()
b.child()

c = C()
c.parent()
c.child()