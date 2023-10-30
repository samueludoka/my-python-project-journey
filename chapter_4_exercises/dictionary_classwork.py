d = {}
print(type(d))

roman_figure = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "XV": 5,
}
print(len(roman_figure))
for k, v in roman_figure.items():
    print(k, v)

for k in roman_figure.keys():
    print(k)
for k in roman_figure.values():
    print(k)

print(roman_figure['II'])
print(roman_figure.get('III'))
roman_figure['XV'] = 15
roman_figure['XXX'] = 30
roman_figure.update({'L': 50, "C": 100})
print(roman_figure)

print('III' in roman_figure)
print('III' not in roman_figure)
print(roman_figure)

roman_figure1 = dict({"i": 1, 'ii': 2, 'iii': 3})
print(roman_figure is roman_figure1)

# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print({n: n ** 2 for n in range(1, 6)})

x = set()
print(x)
x = set({1, 2, 3, 4, 5, 5, 6})
print(x)
