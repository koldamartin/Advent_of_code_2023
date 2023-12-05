with open('aoc_4.txt') as f:
  contents = f.readlines()

result_sum = 0
scores = [1 for z in range(len(contents))]

for x in range(len(contents)):
    winning_numbers = list(filter(None, contents[x].split(":")[1].split("|")[0].strip(" ").split(" ")))
    my_card_numbers = list(filter(None, contents[x].split("|")[1].strip(" ").replace("\n","").split(" ")))

    points = 0
    winning_cards = 0
    first = True
    
    for i in range(len(winning_numbers)):
        if winning_numbers[i] in my_card_numbers and first:
            points += 1
            winning_cards += 1
            first = False
        elif winning_numbers[i] in my_card_numbers:
            points *= 2
            winning_cards +=1

    result_sum += points    

    # Solution to part 2:
    for y in range(scores[x]):
        for j in range(winning_cards):
            scores[x+j+1] += 1
        
print(f'The solution to part 1 is {result_sum}')
print(f'The solution to part 2 is {sum(scores)}')
