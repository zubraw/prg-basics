movie_title = input('Movie name: ')
director = input('Director: ')
lead_actor = input('Lead actor: ')

file_name = 'movie_details.txt'

with open(file_name,'w') as file:
    file.write('==========================\n')
    file.write(f'Movie name: {movie_title}\n')
    file.write(f'Director: {director}\n')
    file.write(f'Lead Actor: {lead_actor}\n')
    file.write('==========================\n')

print(f'Movie details have been written to {file_name}')
