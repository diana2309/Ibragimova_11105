from abc import abstractmethod, ABC

class Laptop(ABC):
    def pattern(self):
        self.get_buttons()
        self.__str__()
        self.get_buttons_second_language()
        self.get_button_info()
        self.button_name()
        self.get_button_list()
        self.popular_shortcuts_matrix()




    def get_buttons(self):
        print(f'was pressed button')

    def get_buttons_second_language(self):
        print(f'the second language of pressed button')


    def get_button_info(self):
        pass

    def button_name(self):
        pass

    def popular_shortcuts_matrix(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_button_list(self):
        pass


class Button:
    def __init__(self, sign: chr):
        self.sign = sign
        self.another_sign = None

    def __get__(self):
        return self.sign

    def get_buttons(self):
        print(f'was pressed button{self.sign}')

    def get_buttons_second_language(self):
        print(f'the second language of pressed buttons {self.another_sign}')

class ShortCut:
    def __init__(self):
        self.signs = []
        self.another_sign = []

    def get_buttons(self):
        print(f'was pressed button{self.signs}')

    def get_buttons_second_language(self):
        print(f'the second language of pressed button{self.signs} is {self.another_sign}')

class Keyboard:
    def __init__(self, Button):
        self.Button = Button

    def __iter__(self):
        return self.Button


a = Keyboard([Button('z'), Button('s')])
for i in a.__iter__():
    print(i.__get__())



