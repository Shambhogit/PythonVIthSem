"""Write a python program to create a class to print an integer and a character
with two methods having the same name but different sequence of the integer and the
character parameters """


class Overloading:

    def print_string_number(self, a: int, b: str):
        print(a)
        print(b)

    def print_string_number(self, a: str, b: int):
        print(a)
        print(b)


a = Overloading()
a.print_string_number(10, "shambho")
a.print_string_number("shambho", 44)
