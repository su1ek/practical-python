# bounce.py
#
# Exercise 1.5

num_ofBounces = 0
height = 100 # meters
for i in range(10):
    num_ofBounces += 1
    height = height * 3 / 5
    print(num_ofBounces, round(height, 4))