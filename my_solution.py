import sys

dig_str = sys.argv[1]

s = 0
for k in dig_str:
    s += int(k)

print(str(s), end="")
