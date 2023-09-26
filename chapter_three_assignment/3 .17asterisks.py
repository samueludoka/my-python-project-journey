
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
# for rows in range(10):
#     for columns in range(rows):
#         print("*", end='')
#     for row in range(rows, 10):
#         print("", end="")
#     for columns in range(rows, 10):
#         print("*", end="")
#     for row in range(rows, 10):
#         print("", end="")
#     print()
