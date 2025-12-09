# class definition
class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
        return f'Permormer: {self.performer}\n Title:  '
   #DOKOŃCZ ZADANIE
       
    
    
# object creation
song1 = ...
song2 = ...

## object usage
print(song1)
...