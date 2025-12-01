input = [(-1 if rotation[:1] == "L" else 1, int(rotation[1:])) for rotation in map(str.strip, open("test_input.txt").readlines())]
print(input)
def part1(input):
    current_num = 50
    counter = 0
    for dir, amount in input:
        current_num = (current_num + (amount * dir)) % 100
        if current_num == 0:
            counter += 1

    return counter

def part2(input):
    current_num = 50
    counter = 0
    for dir, amount in input:
        sum = (current_num + (amount * dir))
        print('sdfsdf' + str(sum))
        if sum < 0:
            counter += abs(sum) // 100 + 1
            print(abs(sum) // 100 + 1)
        elif sum >= 0:
            counter += abs(sum) // 100
            print(abs(sum) // 100)

        current_num = sum % 100
        # if current_num == 0:
        #     counter += 1
    return counter

ans1 = part1(input)
ans2 = part2(input)

print(f"Ans 1 = {ans1}, \nAns 2 = {ans2}.")