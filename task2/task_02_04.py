a, b = int(input()), int(input())
while a % b: a, b = b, a % b
print(b)
