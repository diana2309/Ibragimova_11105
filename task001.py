# по привычке назвала задание на 1 контрольной как задание из домашки и теперь в файле task001 код первого задания контрольной



from abc import ABC, abstractmethod


class Music(ABC):
    def __init__(self, timbre, duration, volume):
        self.timbre = timbre
        self.duration = duration
        self.volume = volume
    @abstractmethod
    def music_playback(self):
        pass


    def music_characteristics_output(self):
        return f'the duration of composition:{self.duration} the timbre of composition:{self.timbre}'

    def sound_check(self):
        if 15 <= self.volume <= 60:
            print('Playback is in a safe audio range')
        if self.volume < 15:
            print('Volume needs to be increased')
        if self.volume > 60:
            print('Volume needs to turn down')


class Album(Music):
    def __init__(self, playback_language, author: False):
        self.playback_language = playback_language
        self.author = author

    def music_playback(self):
        super().music_playback()
        print(self.author, "'s Album playback starts now on", self.playback_language, "language")

    def sound_check(self):
        print(self.author, "should be listened to at the highest possible volume")

    def author_existence(self):
        if isinstance(self.author, str):
            return self.author

        else:
            print('please input the real author')




class MusicGroup(Music):
    def __init__(self, group_name, members_count, **kwargs):
        self.members_count = members_count
        self.group_name = group_name
        super().__init__(**kwargs)

    def music_playback(self):
        super().music_playback()
        print(self.group_name, "'s song playback starts now, please rate it")

    def music_characteristics_output(self):
        return f'the duration of composition:{self.duration} the timbre of composition:{self.timbre}' \
               f'the group name of composition:{self.group_name}'

    def __str__(self):
        print('in', self.group_name, "there are", self.members_count, 'wonderful people')

"""Task001b"""

class Song(Album, MusicGroup):
    def __init__(self, song_name, release_date):
        self.song_name = song_name
        self.release_date = release_date

    def song_age(self):
        if self.release_date < 2020:
            print("It's an old song")
        else:
            print("It's a new song")

    def advice(self):
        print("You should listen to the", self.song_name, "of", self.release_date, "release date")



if __name__ == '__main__':
    album1 = Album('korean', '3racha')
    album2 = Album("english", 'halsey')
    album3 = Album('russian', 3)
    album1.music_playback()
    album2.music_playback()
    album3.author_existence()

    albums = [album1, album2, album3]


    music1 = MusicGroup(timbre = 'sharp', duration = 3.5, volume = 100, members_count = 8, group_name = 'Stray kids')
    music2 = MusicGroup(timbre = 'soft', duration = 2, volume = 34, members_count = 5, group_name = 'TXT')
    music1.music_playback()
    music1.__str__()
    music1.music_characteristics_output()
    music1.sound_check()
    music2.music_playback()
    music2.music_characteristics_output()
    music2.sound_check()

    music = [music1, music2]

    music4 = Song("God's menu", 2020)
    music4.advice()
    music4.song_age()


print(albums, music)
