class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f'Performer: {self.artist} \nTitle: {self.title} \nAlbum: {self.album}\nYear: {self.year}'

song1 = Song('Kendrick Lamar', 'Not like us', '-single-', 2024)
song2 = Song('Kanye West', 'Stonger', 'Graduation', 2007)

print(song1)
print(song2)