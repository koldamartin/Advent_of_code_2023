with open('aoc_1.txt') as f:
    contents = f.readlines()

numbers_list = []

for line in contents:
    for first_letter in line:
        if first_letter.isdigit() is True:
            break
    
    for last_letter in reversed(line):
        if last_letter.isdigit() is True:
            break
        
    numbers_list.append(int(str(first_letter)+str(last_letter)))   
    
print(f"Sum of numbers is {sum(numbers_list)}")
