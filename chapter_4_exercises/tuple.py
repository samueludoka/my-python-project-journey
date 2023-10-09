from tkinter.font import names

print(id(names))
tuple1 = 1, 2, 'divine'
tuple2 = 4
tuple1 += tuple2
tuple1 = tuple1 + tuple2
print(tuple1)
print(id(names))
