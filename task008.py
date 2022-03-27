
class Button:
    def __init__(self, sign: chr):
        self.sign = sign

    def __get__(self):
        return self.sign


class Keyboard:
    def __init__(self, Button):
        self.Button = Button

    def __iter__(self):
        return self.Button


a = Keyboard([Button('z'), Button('s')])
for i in a.__iter__():
    print(i.__get__())
