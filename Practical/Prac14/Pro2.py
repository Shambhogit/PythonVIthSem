
class Shep:

    def area(self, length=None, breadth=None):
        if breadth == None:
            print("Area of Square is : ", length * length)
        elif length != None and breadth != None:
            print("Area of rectangle is : ", length * breadth)
        else:
            print("Invlid input")


s = Shep()
s.area(10)
s.area(10,20)

