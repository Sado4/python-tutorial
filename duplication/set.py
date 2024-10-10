# 集合
x = {1, 2, 4}
y = {1, 2, 3, 4, 5}
print(x)

x.add(3)

print(x)

x.remove(3)

print(x)

# 和集合
z = x | y

print(z)

# 積集合
z = x & y

print(z)

# 差集合
z = y - x

print(z)
