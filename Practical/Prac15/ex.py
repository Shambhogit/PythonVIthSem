#mport google.protobuf.text_encoding


class Animal:
    multi = True
    euka = True

    def breathe(self):
        print("i breathe oxygen")

    def feed(self):
        print("i eat food")

class Herbi(Animal):
    def feed(self):
        print("i eat on;u plants")

h = Herbi()
h.feed()
h.breathe()