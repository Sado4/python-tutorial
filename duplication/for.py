# for文
for i in range(5):
    print(i)

for i in range(7, 10):
    print(i)

# 辞書
scores = {
    "数学": 82,
    "国語": 74,
    "英語": 60,
    "理科": 92,
    "社会": 70,
}


# for文(辞書)
for key, value in scores.items():
    print(key, value)
