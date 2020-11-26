
class Cow:
    def __init__(self, name, weight=0, milk=0):
        self.name = name
        self.weight = weight
        self.milk = milk

    def take_milk(self,):
        if self.milk > 0:
            self.milk -= 1
        else :
            print('Молока нет!')

    def feed(self):
        self.weight += 1

class Sheep:
    def __init__(self, name, weight=0, wool=0):
        self.name = name
        self.weight = weight
        self.wool = wool

    def take_wool(self):
        if self.wool > 0:
            self.wool -= 1
        else:
            print('Шерсти нет')

    def feed(self):
        self.weight += 1


class Chicken:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.weight = weight
        self.eggs = eggs

    def take_eggs(self,):
        if self.eggs > 0:
            self.eggs -= 1
        else :
            print('Яиц нет!')

    def feed(self):
        self.weight += 1


class Goat:
     def __init__(self, name, weight=0, milk=0):
        self.name = name
        self.weight = weight
        self.milk = milk

     def take_milk(self,):
        if self.milk > 0:
            self.milk -= 1
        else :
            print('Молока нет!')

     def feed(self):
        self.weight += 1

class Duck:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.weight = weight
        self.eggs = eggs

    def take_eggs(self,):
        if self.eggs > 0:
            self.eggs -= 1
        else :
            print('Яиц нет!')

    def feed(self):
        self.weight += 1

class Geese:
    def __init__(self, name, weight=0, eggs=0):
        self.name = name
        self.weight = weight
        self.eggs = eggs

    def take_eggs(self,):
        if self.eggs > 0:
            self.eggs -= 1
        else:
            print('Яиц нет!')

    def feed(self):
        self.weight += 1


g_geese = Geese('Серый', 10, 3)
w_geese = Geese('Белый', 11, 4)
m_cow = Cow('Манька', 93, 1)
b_sheep = Sheep('Барашек', 75, 3)
k_sheep = Sheep('Кудрявый', 70, 3)
ko_chicken = Chicken('Ко-Ко', 15, 1)
ku_chicken = Chicken('Кукареку', 12, 0)
r_goat = Goat('Рога', 50, 12)
k_goat = Goat('Копыта', 53, 10)
kr_duck = Duck('Кряква', 18, 2)

def weight_all():
    list = [ g_geese,
             w_geese,
             m_cow,
             b_sheep,
             k_sheep,
             ko_chicken,
             ku_chicken,
             r_goat,
             k_goat,
             kr_duck,
            ]
    weight_final = 0
    for a in list:
        weight_final += a.weight
    return weight_final

def biggest():
    list = [g_geese,
            w_geese,
            m_cow,
            b_sheep,
            k_sheep,
            ko_chicken,
            ku_chicken,
            r_goat,
            k_goat,
            kr_duck,
            ]
    weight_biggest = 0
    weight_biggest_name = 0
    for a in list:
        if a.weight > weight_biggest:
            weight_biggest = a.weight
            weight_biggest_name = a.name
    return weight_biggest_name

print(weight_all())
print(biggest())
