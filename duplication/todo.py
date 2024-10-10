# todoをpythonで実装する

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def complete_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

todo = Todo()

todo.add_task("タスク1")
todo.add_task("タスク2")
todo.add_task("タスク3")

todo.show_tasks()

todo.delete_task("タスク2")

todo.show_tasks()

todo.complete_task("タスク1")

todo.show_tasks()
