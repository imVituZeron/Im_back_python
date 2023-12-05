classrooms = [
    ["maria", "helena"],
    ["Vitor"],
    ["Sara", "Eliza", "Leandro", (0,10,20,30,40)]
]

print(classrooms[2][3][2])

for classroom in classrooms:
    print(f"The classroom is {classroom}")
    for student in classroom:
        print(f"\t{student}")