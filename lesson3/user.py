class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_firstname(self):
        print(f'Моё имя: {self.first_name}')

    def print_lastname(self):
        print(f'Моя фамилия: {self.last_name}')

    def print_allname(self):
        print(f'Мои имя и фамилия: {self.first_name} {self.last_name}')
