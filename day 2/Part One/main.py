import re

file = open('../input.txt', 'r')
game_dict = {}
pattern1 = r'(\d+)(?=:)'
result = []
i = 0
aux_list = []
for j in range(100):
    aux_list.append(j)
for line in file:
    matches = re.findall(pattern1, line)
    if matches:
        game = matches[0]
        print(game)
        pattern = r'(\d+)\s(\w+)'
        matches = re.findall(pattern, line)
        print(matches)
        for match in matches:
            digit = int(match[0])
            color = match[1]
            if (color == 'red' and digit > 13) or (color == 'blue' and digit > 14) or (color == 'green' and digit > 15):
                aux_list.remove(int(game))
                break
print("Result:", result)
print(sum(result))
