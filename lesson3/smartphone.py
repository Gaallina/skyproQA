class Smartphone:
    def __init__(self, marka, model, number):
        self.marka = marka
        self.model = model
        self.number = number

    def print_info(self):
        print(f'{self.marka} - {self.model}. {self.number}')
