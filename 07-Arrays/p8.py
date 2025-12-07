#Write a program that prints a popular computer games, each game name on a separate line. 
# Use the while statement. Additionally, number the list 
# (print the next number before each list item) 
# and sort the list alphabetically (use one of a Python built-in functions for sorting)

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
n = len(computer_games)
i = 1
sorted_games = sorted(computer_games)
while i <= n:
    print(f'{i}. {sorted_games[i-1]}')
    i = i + 1