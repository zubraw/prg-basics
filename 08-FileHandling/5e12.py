import csv
with open('books.csv','r') as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        book_genre = f'books_{row[2].lower()}.txt'
        with open(book_genre,'a') as genre:
            genre.write(f'{row}\n')