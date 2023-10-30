names = ["ope", "qudus", "divine"]
a, b, c = names
print(a, b, c)

names2 = list("isreal")
tuple1 = 1, 2, 3
tuple2 = 'a', 'b', 'c'

list_to_tuple = tuple(names)
print(list_to_tuple)

tuple_toList = list(list_to_tuple)
print(tuple_toList)

print(names + names2)
names += "isreal"

# tuple1 += names
# this cant work

names[0] = "tosin"
print(names)

# tuple1[0] = 'p'
# print(tuple1)

tuple3 = 1, 2, 3, "ope", ["precious", "joy"], "delighted"
tuple3[4][0] = "mercy"
print(tuple3)

tuple3 = 1, 2, 3, "ope", ["precious", "joy"], "delighted"
lt = list(tuple3)
lt[3] = "tobi"

lt = tuple(lt)
print(lt)

tuple3 = 1, 2, 3, "ope", ["precious", "joy"], "delighted"
ans = tuple3[1] * 5
print(ans)

a = (1, (2, 3), ("a", "b"), 4, [5, 6], True)
print(a)

b = ["ope", "arua", "joy", (1, 2), [3, 4]]
print(b)

tuple1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x, y, *others = tuple1
print(x, y, others)

tuple1 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x, *others, y = tuple1
print(x, others, y)

# to delete an element in a list u use del keyword
names = ["ope", "qudus", "divine"]
del names[1]
print(names)

del names[:]
print(names)

names = ["ope", "qudus", "divine"]
names.append("precious")
names.sort(reverse=True)
print(names)

names = ["ope", "qudus", "divine"]
n = sorted([11, 7, 5, 3, 1])
print(n)

n = sorted([11, 7, 5, 3, 1])
n.extend([4, 5, 6, 7])
print(n)

print(names.index("ope"))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers *= 2
print(numbers)
print(numbers.index(5, 7))

# names.pop(1)
# print(names)

names.remove('ope')
print(names)

names = ["ope", "qudus", "divine"]
copy_of_names = names.copy()
copy_of_names2 = names[:]
print(copy_of_names2)
print(copy_of_names)

numbers.index(3, 5)
print(numbers.count(3))

numbers.index(3, 5)
print(any(numbers))


def my_index(li: list, n):
    idx = 0
    for i in range(len(li)):
        if li[i] == li:
            idx = i
    return idx


print(numbers)
print(my_index(numbers, 3))


def my_index(li: list, n):
    idx = 0
    for i in range(len(li)):
        if li[i] == li:
            idx = i
    return idx


def even_check(n):
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ans = 0
    if n % 2 == 0:
        ans = 0
    return ans


even_list = filter(even_check, numbers)
print(list(even_list))

result = [i for i in range(1, 11) if i % 2 == 0]
print(result)
