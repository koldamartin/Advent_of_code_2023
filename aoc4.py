with open('aoc_4.txt') as f:
  contents = f.readlines()

result_sum = 0

for line in contents:
    winning_numbers = list(filter(None, line.split(":")[1].split("|")[0].strip(" ").split(" ")))
    my_card_numbers = list(filter(None, line.split("|")[1].strip(" ").replace("\n","").split(" ")))

    points = 0
    first = True
    for number in winning_numbers:
        if number in my_card_numbers and first:
            points += 1
            first = False
        elif number in my_card_numbers:
            points *= 2
    
    result_sum += points    
    
print(f'The result is {result_sum}')