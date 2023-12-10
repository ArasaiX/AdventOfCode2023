def parse_cube(cube):
    cube_dict = {}
    bag = cube.strip().split(': ')
    plays = bag[1].split('; ')
    for play in plays:
        combinations = play.split(', ')
        for combination in combinations:
            quantity, color = combination.split(' ')
            if color not in cube_dict or int(quantity) > cube_dict[color]:
                cube_dict[color] = int(quantity)
    return cube_dict
    
file = open('../input.txt', 'r')
sum = 0
for line in file:
    game_dict = parse_cube(line)
    aux_value = 1
    for value in game_dict.values():
        aux_value *= value
    sum = sum + aux_value
file.close()
print("Sum of the power of sets:", sum)