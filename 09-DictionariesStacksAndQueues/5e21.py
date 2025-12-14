import json
fav_movie ={
    'title': 'Notebook',
    'year' : 2004,
    'actor' : 'Ryan Gosling',
    'genre' : 'Romantic',
    'grade' : 4.7
}

with open('favourite.json','w') as file:
    string = json.dumps(fav_movie, indent=4)
    file.write(string)