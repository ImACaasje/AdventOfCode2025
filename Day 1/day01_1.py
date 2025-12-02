input = [(-1 if rotation[:1] == "L" else 1, int(rotation[1:])) for rotation in map(str.strip, open("input.txt").readlines())]
current_num = 50
counter = 0
for dir, amount in input:
    current_num = (current_num + (amount * dir)) % 100
    if current_num == 0:
        counter += 1
print(f"ans: {counter}")