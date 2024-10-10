# if文
x = 10

if x > 0:
    print("xは正の数です")
elif x == 0:
    print("xは0です")
else:
    print("xは負の数です")

# in
x = 10

if x in [1, 2, 3, 4, 5]:
    print("xは1から5の間の数です")
else:
    print("xは1から5の間の数ではありません")

# and
x = 10
y = 20

if x > 0 and y > 0:
    print("xとyは正の数です")
else:
    print("xとyは正の数ではありません")
    

# or
x = 10
y = 20

if x > 0 or y > 0:
    print("xかyは正の数です")
else:
    print("xかyは正の数ではありません")

# not
x = 10

if not x > 0:
    print("xは正の数ではありません")
else:
    print("xは正の数です")
    

# is
x = 10
y = 10

if x is y:
    print("xとyは同じオブジェクトです")
else:
    print("xとyは同じオブジェクトではありません")
    
