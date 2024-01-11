l = []
for x in range(3):
    for y in range(3):
        l.append((x, y))

# for into for in list comprehension
l = [(x, y) for x in range(3) for y in range(3)]

print(l)
