input = [range.strip().split(',') for range in open("input.txt").readlines()][0]
ans = 0

for r in input:
  for i in range(int(r.split('-')[0]), int(r.split('-')[1]) + 1):
    s = str(i)
    if len(s) % 2 != 0:
      continue
    if s[:len(s)//2] == s[len(s)//2:]:
      print(f"invalid: {i}")
      ans += i

print(f"ans = {ans}")