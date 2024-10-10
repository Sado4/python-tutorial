# private変数
# private変数とは、クラスの外部からアクセスできない変数

class MyClass:
    def __init__(self):
        self.__private_variable = 10

    def get_private_variable(self):
        return self.__private_variable

my_class = MyClass()
print(my_class.get_private_variable())

# エラーになる例
print(my_class.__private_variable)
