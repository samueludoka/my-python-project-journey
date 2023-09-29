
for row in range(20):
    for s in range(row):
        print("*", end="")
    for q in range(row, 20):
        print(" ", end="")
    for column in range(row, 20):
        print("*", end="")
    for p in range(row):
        print(" ", end="")
    for f in range(row):
        print(" ", end="")
    for z in range(row, 20):
        print("*", end="")
    print()
