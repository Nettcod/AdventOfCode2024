mul_enabled = True

def main():
    input = open("./input", "r").read()

### Part One ###
    multiplication_sum = 0
    i = 0
    while True:
        i = input.find("mul(", i)
        if i == -1:
            break
        i = i + 4
        j = input.find(")", i)
        if (j - i) <= 7:
            substr = input[i:j]
            multiplication_sum = multiplication_sum + find_product(substr)
            i = j + 1
    print("Part one: " + str(multiplication_sum))

### Part Two ###
    global mul_enabled
    multiplication_sum = 0
    i = 0
    while True:
        i = parse_next_instruction(input)
        if i == -1:
            break
        i = input.find("mul(", i)
        i = i + 4
        j = input.find(")", i)
        if (j - i) <= 7 and mul_enabled == True:
            substr = input[i:j]
            multiplication_sum = multiplication_sum + find_product(substr)
            i = j + 1
        input = input[i:]
    print("Part two: " + str(multiplication_sum))


def find_product(s:str):
    args = s.split(",") 
    if args[0].isnumeric() and args[1].isnumeric():
        x = int(args[0])
        y = int(args[1])
        if abs(x) > 999 or abs(y) > 999:
            return 0
        return x * y
    return 0 


def parse_next_instruction(s:str):
    next_mul_index = s.find("mul(")
    next_do_index = s.find("do()")
    next_dont_index = s.find("don't()")
    global mul_enabled    
    if (next_do_index < next_dont_index or next_dont_index == -1) and next_do_index != -1 and next_do_index < next_mul_index:
        mul_enabled = True
        return next_do_index + 4
    elif next_dont_index < next_mul_index and next_dont_index != -1:
        mul_enabled = False
        return next_dont_index + 7
    return next_mul_index    


main()
