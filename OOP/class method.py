class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name} {self.age}'

q1= Person('tien',22)
print(q1)

#Multiple methods
class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f'Add: {song}')
    def remove_song(self,song):
        self.songs.remove(song)
        print(f'Removed {song}')
    def show_song(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f' {song}')
        
my_playlist= Playlist('Favourites')
my_playlist.add_song('noi nay co em')
my_playlist.add_song('noi nay co anh')
my_playlist.show_song()
my_playlist.remove_song('noi nay co em')
my_playlist.show_song()

