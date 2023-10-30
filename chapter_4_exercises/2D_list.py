
my_list = []
new_list = [[0 for col in range(3)] for row in range(2)]

for i in range(2):
    for j in range(3):
        new_list[i][j] = i*j
print(new_list)

