# クラス
class User:
    def __init__(self, name, age, mail_address, point):
        self.name = name
        self.age = age
        self.mail_address = mail_address
        self.point = point

    def hello(self):
        print("Hello, " + self.name)

    def add_point(self, point):
        self.point += point

# class Shop:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def hello(self):
#         print("Hello, " + self.name)

# インスタンス
# user = User(name="Alice", age=20, mail_address="alice@example.com", point=100)
# shop = Shop(name="Bob", price=100)

# インスタンスメソッド
user_1 = User(name="Alice", age=20, mail_address="alice@example.com", point=100)
user_2 = User(name="Bob", age=30, mail_address="bob@example.com", point=200)

user_1.add_point(point=100)
user_2.add_point(point=200)

# user_1.hello()
# user_2.hello()

print(user_1.point)
print(user_2.point)
