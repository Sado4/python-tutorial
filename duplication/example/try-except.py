# 例外処理

try:
    # 例外が発生する処理
    print(100 / 0)
except ZeroDivisionError:
    # 例外が発生した場合の処理
    print("例外が発生しました")
finally:
    # 例外が発生してもしなくても実行される処理
    print("終了")
