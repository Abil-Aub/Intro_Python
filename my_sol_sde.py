import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

disc = b*b - 4*a*c # Discriminant

x1 = (-b - math.sqrt(disc))/(2*a) # First solution
x2 = (-b + math.sqrt(disc))/(2*a) # Second solution

print(int(x1))
print(int(x2))
