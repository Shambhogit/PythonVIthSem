class Degree:
    def getDegree(self):
        print("I got a Degree")


class Undergraduate(Degree):
    def getDegree(self):
        print("I got a Undergraduate")


class Postgraduate(Degree):
    def getDegree(self):
        print("I got a Postgraduate")


d = Degree()
u = Undergraduate()
p = Postgraduate()

d.getDegree()
u.getDegree()
p.getDegree()

