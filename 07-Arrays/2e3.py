# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_total = 0
transport_total = 0
utilities_total = 0
total = 0
for row in monthly_expenses:
    food_total += row[0]
    transport_total += row[1]
    utilities_total += row[2]
    for item in row:
        total += item



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food: ',food_total)
print('Transport: ',transport_total)
print('Utilities: ', utilities_total)
week = 1
for rows in monthly_expenses:
    week_total = 0
    for items in rows:
        week_total += items
    print(f'Week {week}: {week_total}')
    week +=1
print('---------------')
print('TOTAL:', total)