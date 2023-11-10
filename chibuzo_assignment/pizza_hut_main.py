import chibuzo_assignment.pizza_hut
from pizza_hut import box_size, number_of_hungry_persons

box_sizes = str(input("Enter smallBox, mediumBox, largeBox for box_size: "))
super_hungry1 = int(input("Enter number of super hungry persons: "))
normal_hungry1 = int(input("enter number of normal hungry persons: "))
classic_hungry1 = int(input("Enter number classic hungry: "))

pizza_box_size = box_sizes
print(box_size(box_sizes))
number_of_hungry_persons = super_hungry1 + normal_hungry1 + classic_hungry1
print(f""""
=======================================================
box selected is {box_size}
number of hungry people is {super_hungry1}
number of normal hungry people is {normal_hungry1}
number of classic hungry people is {classic_hungry1}
=======================================================
""")
