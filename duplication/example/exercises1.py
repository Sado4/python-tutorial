# 問題1
scores = {
  "数学": 82,
  "国語": 74,
  "英語": 60,
  "理科": 92,
  "社会": 70,
}

score = scores["理科"] - scores["社会"]

print(f"{score}点")

# 平均点を求める
average = sum(scores.values()) / len(scores)

print(f"{average}点")
