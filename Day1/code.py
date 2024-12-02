def main():
### Part One ###
    input = open("./input", "r")

    list_1 = []
    list_2 = []

    for line in input:
        values = line.split("   ")
        list_1.append(int(values[0]))
        list_2.append(int(values[1]))

    list_1.sort()
    list_2.sort()

    distance = 0

    for i in range (0, len(list_1), 1):
        local_distance = abs(list_1[i] - list_2[i])
        distance = distance + local_distance

    print('Part 1: ' + str(distance))

### Part Two ###
    similarity = 0

    for value in list_1:
        local_similarity = value * list_2.count(value)
        similarity = similarity + local_similarity

    print('Part 2: ' + str(similarity))


main()
