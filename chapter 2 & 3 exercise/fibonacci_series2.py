
eseries = [0, 1]
number = 10
if number > 2:
    for i in range(2, number):
        num = eseries[i - 1] + eseries[i - 2]
        eseries.append(num)
    print(eseries)
