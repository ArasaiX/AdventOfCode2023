import re

file = open('../input.txt', 'r')
game_dict = {}
pattern_game = r'(\d+)(?=:)'
result = list(range(1, 101))

for line in file:
    matches = re.findall(pattern_game, line)
    if matches:
        game = matches[0]
        pattern = r'(\d+)\s(\w+)'
        matches = re.findall(pattern, line)
        for match in matches:
            digit = int(match[0])
            color = match[1]
            if (color == 'red' and digit > 12) or (color == 'green' and digit > 13) or (color == 'blue' and digit > 14):
                result.remove(int(game))
                break
print("Games:", result)
print("Sum od IDs:", sum(result))

