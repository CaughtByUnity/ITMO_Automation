class Soda:
    def __init__(self, taste = None):
        self.taste = taste
    def show_my_drink(self):
        if self.taste:
            print(f'Газировка и {self.taste}')
        else:
            print('Обычная газировка')
coke = Soda('coca')
coke.show_my_drink()
richalsu = Soda()
richalsu.show_my_drink()