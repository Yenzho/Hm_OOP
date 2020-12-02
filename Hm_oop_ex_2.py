class Track:
    def __init__(self, name, duration,):
        self.name = name
        self.duration = duration

    def __str__(self):
            return f'{self.name} - {self.duration}'

    def __lt__(self, other):
        if not isinstance(other, Track):
            print('Это не трек')
        return self.duration < other.duration



class Album:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.all_tracks = []

    def get_tracks(self):
        all_tracks = []
        if not self.all_tracks:
            print('Треков нет')
        else:
            for tr in self.all_tracks:
                 all_tracks.append(tr.__str__())
        return "\n".join(all_tracks)

    def __str__(self):
        list_tracks = []
        for t in self.all_tracks:
            list_tracks.append(t.__str__())

        A = f'Name group: {self.group}\nName album: {self.name}\nTracks: \n\t    '
        B = "\n\t\t".join(list_tracks)
        return A+B

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
print(work)
print(serega)





