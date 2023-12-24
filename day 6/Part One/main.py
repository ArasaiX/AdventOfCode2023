from functools import reduce

def calculate_ways(time, distance):
    total = 0
    for i in range(time):
        time_rest = (time - (i + 1))
        distance_final = time_rest * (i+1)
        if distance_final > distance:
            total += 1
    return total

with open("../input.txt", "r") as file:
    data = [[int(element) for element in line.split() if element.isdigit()] for line in file.read().split('\n') if line]
result = []
for i in range(len(data)-1):
    for j in range(len(data[i])):
        result.append(calculate_ways(data[i][j], data[i + 1][j]))
print("Multiplication of total ways: ", reduce(lambda a, b: a*b, result))