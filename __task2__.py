import math
x = 0.712
y = 3.161

a = (x * y**2) + (y * math.sin(x)) + (142 * x**2) * y
b = (math.tan(x * y) - (142 * (y - x)) / 16.32)
c = a + b
print(c) if a >= 0 else print("Розвязків немає")
