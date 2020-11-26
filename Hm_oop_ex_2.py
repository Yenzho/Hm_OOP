class Track:
    def __init__(self, name, duration,):
        self.name = name
        self.duration = duration


    def show(self):
        print(f'<{self.name} - {self.duration}>')

class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.all_tracks = []

    def get_tracks(self):
        if not self.all_tracks:
            print('Треков нет')
        else:
            for tr in self.all_tracks:
                tr.show()

    def add_track(self):
        self.all_tracks.append()


    def get_duration(self):
        full_duration = 0
        for tr in self.all_tracks:
            full_duration += tr.duration
        return full_duration

serega_why = Track('Серега почему', 25)
dolgy = Track('Долги', 42)
net_deneg = Track('Нет денег', 100)
work = Track('Работа', 124)
mom = Track('Мать', 164)
wow = Track('Вау', 156)

serega = Album('Серега', 'Наркоманы')
serega.all_tracks = [serega_why, dolgy, net_deneg]

boring = Album('Скучный', 'Балбесы')
boring.all_tracks = [wow, work, mom]


print(serega.get_duration())
print(boring.get_duration())

