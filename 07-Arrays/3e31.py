array = [[-38, 19], [5,40],[-7,11],[29,16]]
min_val = array[0][0]
min_row = 0
min_col = 0
max_val = array[0][0]
max_row = 0
max_col = 0
for row in range(len(array)):
    for col in range(len(array[row])):
        value = array[row][col]
        if value < min_val:
            min_val = value
            min_row = row
            min_col = col
        
        if value > max_val:
            max_val = value
            max_row = row
            max_col = col
print(f'Max value: {max_val}, ({max_row},{max_col})')

print(f'Min value: {min_val}, ({min_row},{min_col})')

    
        