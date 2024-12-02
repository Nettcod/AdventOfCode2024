def main():
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

    print(distance)


main()
