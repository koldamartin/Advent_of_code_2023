with open('aoc_2.txt') as f:
  contents = f.readlines()

RED = 12
GREEN = 13
BLUE = 14
# Result for part 1
sum_result = 0
# Result for part 2
sum_of_power_result = 0

# Loop through each line
for line in contents:
  
  # Get the game number
  game_no = int((line.split(" "))[1].split(":")[0])
  
  rest = line[line.find(":") + 1: ]
  rest_list = rest.split(";")
  
  game_set_list =[]
  list_of_dict =[]
  
  # Loop through each set in a game (split on ',')
  for i in range(len(rest_list)):
    game_set_part = rest_list[i].replace(" ", "").split(",")
    game_set_list.append(game_set_part)
    
    # Loop through each colour drawn
    for j in range(len(game_set_list[i])):
      index = 1
      if game_set_list[i][j][1].isdigit():
        index = 2
      # Get the number from each game
      number = game_set_list[i][j][:index]
      # Get the color from each game
      color = game_set_list[i][j][index:].replace("\n","")
      # Create a dictionary e.g. {red:8}
      game_set_dict = {}
      game_set_dict[color] = int(number)
      # Create a list of dictionaries for specific line
      list_of_dict.append(game_set_dict)

  # Solution to part 1
  add_number = True

  for dict in list_of_dict:
    if 'red' in dict and (dict['red']) > RED:
      add_number = False
    if 'blue' in dict and (dict['blue']) > BLUE:
      add_number = False
    if 'green' in dict and (dict['green']) > GREEN:
      add_number = False
  # If not, then make a sum of game_no
  if add_number == True:   
    sum_result += game_no

  # Solution to part 2
  reds=[]
  blues=[]
  greens=[]
  for dict in list_of_dict:
    if 'red' in dict:
      reds.append(dict['red'])
    if 'blue' in dict:
      blues.append(dict['blue'])
    if 'green' in dict:
        greens.append(dict['green'])
  power_line = max(reds) * max(blues) * max(greens)
  sum_of_power_result += power_line

# PART 1
print(f"The result of part 1 is {sum_result}")

# PART 2
print(f"The result of part 2 is {sum_of_power_result}")