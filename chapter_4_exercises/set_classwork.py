my_set = {1, 1.1, "ope", 1, 2, "ope"}
print(my_set)

# my_set = {1, 1.1, "ope", 1, 2, "ope", {1, 2, 3}}  # contains an unhashable type or mutable list
# print(my_set)

print(len(my_set))
myset2 = frozenset({1, 3, 5, 7, 9})
empty_set = set()

empty_set.add(4)
empty_set.add("delighted")
print(empty_set)
print(2 in my_set)


for item in my_set:
    print(item, end= ' ')


set1 = set(range(1, 21))
set2 = {1, 4, 3, 5}
print(set1. issuperset(set2))

set3 = {1, 2, 6, 3, 7, 9}
set4 = {1, 4, 3, 5}
print(set3.union(set4))
print(set3 | set4)

set3 = {1, 2, 6, 3, 7, 9}
set4 = {1, 4, 3, 5}
print(set3.intersection(set4))
print(set3 & set4)


set3 = {1, 2, 6, 3, 7, 9}
set4 = {1, 4, 3, 5}
print(set3.difference(set4))
print(set4 - set3)

print(set3.difference(set4))
print(set3.symmetric_difference(set4))

