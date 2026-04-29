class Playlist:
    def __init__(self, name, song_count=0):
        self.name = name
        self.song_count = song_count 

    def set_name(self, name):
        self.name = name
    
    def set_song_count(self, song_count):
        self.song_count =  song_count

    def get_name(self):
        return self.name
    
    def get_song_count(self):
        return self.song_count
    
    def add_song(self):
        self.song_count += 1
        
    
    def remove_song(self):
        if self.song_count > 0:
            self.song_count -= 1
        else:
            print(f"There are no songs in the playlist")

    def show_info(self):
        print(f"Playlist: {self.get_name()}, Total Song(s): {self.get_song_count()}")



playlist = Playlist("Lo-fi")
playlist.add_song()
playlist.add_song()
playlist.add_song()
playlist.show_info()
playlist.remove_song()
playlist.show_info()
playlist.add_song()
playlist.add_song()
playlist.show_info()






