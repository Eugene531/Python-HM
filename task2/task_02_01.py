fr1, fr2 = [list(map(int, input().split("/"))) for _ in ".."]

print(f'Result is {fr1[0] * fr2[1] + fr1[1] * fr2[0]}/{fr1[1] * fr2[1]}')
