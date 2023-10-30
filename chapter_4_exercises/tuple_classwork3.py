
test_list = [
    [0, 0, 0],
    [0, 0, 0]
    ]
# for i in range(len(test_list)):
for i, val in enumerate(test_list):
    for j, _ in enumerate(val):
        test_list[i][j] = 5

print(test_list)

