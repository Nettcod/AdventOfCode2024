path = "./input"

def main():
    input = open(path, "r")

### Part One ###
    char_grid = []
    for line in input:
        char_grid.append(line)

    xmas_count = 0

    width = len(char_grid[0])
    depth = len(char_grid)
    i = 0
    while i < depth:
        j = 0
        while j < width:
            xmas_count = xmas_count + check_horizontal(char_grid, i, j) + check_vertical(char_grid, i, j) + check_diagonal_left_right(char_grid, i, j) + check_diagonal_right_left(char_grid, i, j)
            j = j + 1
        i = i + 1
    print("Part One: " + str(xmas_count))

### Part Two ###
    x_mas_count = 0

    width = len(char_grid[0])
    depth = len(char_grid)
    i = 0
    while i < depth:
        j = 0
        while j < width:
            x_mas_count = x_mas_count + check_x_mas(char_grid, i, j)
            j = j + 1
        i = i + 1
    print("Part Two: " + str(x_mas_count))

            
### Part One helpers ###
def check_horizontal(s:list, i:int, j:int):
    substr = s[i][j:j+4]
    if (substr == "XMAS") or (substr == "SAMX"):
        return 1  
    return 0

def check_vertical(s:list, i:int, j:int):
    substr = ""
    if (i + 4) > len(s):
        return 0
    for k in range(i, i+4, 1):
        substr = substr + s[k][j]
    if (substr == "XMAS") or (substr == "SAMX"):
        return 1
    return 0

def check_diagonal_left_right(s:list, i:int, j:int):
    if ((i + 4) > len(s)) or ((j + 4) > len(s[i])):
        return 0
    substr = ""
    for k in range(0, 4, 1):
        substr = substr + s[i+k][j+k]
    if (substr == "XMAS") or (substr == "SAMX"):
        return 1
    return 0

def check_diagonal_right_left(s:list, i:int, j:int):
    if ((i + 4) > len(s)):
        return 0
    substr = ""
    for k in range(0, 4, 1):
        substr = substr + s[i+k][j-k]
    if (substr == "XMAS") or (substr == "SAMX"):
        return 1
    return 0

### Part Two helpers ###
def check_x_mas(s:list, i:int, j:int):
    if ((i + 3) > len(s)) or ((j + 3) > len(s[i])):
        return 0
    substr_fwd = ""
    substr_bwd = ""
    for k in range(0, 3, 1):
        substr_fwd = substr_fwd + s[i+k][j+k]
        substr_bwd = substr_bwd + s[i+k][j-k+2]
    if ((substr_fwd == "MAS") or (substr_fwd == "SAM")) and ((substr_bwd == "MAS") or (substr_bwd == "SAM")):
        return 1
    return 0

main()
