# override
# overrideとは、親クラスのメソッドを子クラスで上書きすること

class Parent:
    def __init__(self):
        self.value = "Parent"

    def show(self):
        print(self.value)
        

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"

    def show(self):
        print(self.value)


parent = Parent()
parent.show()

child = Child()
child.show()
