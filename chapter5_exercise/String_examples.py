import re

my_digit = '08085678222'
# print("True") if re.fullmatch(r'\d{4}')
print("True" if re.fullmatch(r'\d + [A-z][a-z]*[A-z][a-z]*', 'Cap, Pap') else "False")
