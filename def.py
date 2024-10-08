# 関数
def hello():
    print("Hello, World!")

hello()

# 引数
def hello(name):
    print("Hello, " + name)

hello("Alice")

# 戻り値
def add(a: int, b: int) -> int:
    return a + b

print(add(a=1, b=2))
