def check_points(line):
    line = line.split(': ')
    winner_column, play_column = line[1].split(' |')
    winner_column = winner_column.split(' ')
    play_column = play_column.split(' ')
    winner_numbers = [] 
    play_numbers = []
    points = 0
    for winner in winner_column:
        if winner.isdigit():
            winner_numbers.append(int(winner))
    for play in play_column:
        if play != '':
            play_numbers.append(int(play))
    for i in range(len(play_numbers)):
        if play_numbers[i] in winner_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

try:
    with open("../input.txt", "r") as file:
        result = []
        for line in file:
            points = check_points(line)
            result.append(points)
    print("The sum of points are: ", sum(result))
except FileNotFoundError:
    print("File not found.")
