class Plane:
    def __init__(self, made_in, number_of_seats, number_of_rows, passengers=40):
        self.made_in = made_in
        self.number_of_seats = number_of_seats
        self.number_of_rows = number_of_rows
        self.passengers = passengers

    def calc_total_number_of_seats(self):
        return self.number_of_seats * self.number_of_rows

    def __str__(self):
        return f'The plain is made in {self.made_in}'

    @classmethod
    def plane_fullness(cls):
        a = cls.passengers/(cls.calc_total_number_of_seats())
        return f'the fullness is{a}%'

    @staticmethod
    def plane_speed(speed, name):
        return f'The plain{name} is flying at a speed of {speed} km/h'


pl1 = Plane('Russia', 20, 3)
print(pl1.calc_total_number_of_seats())
print(pl1.plane_speed(700, 'uhngfijdks'))
