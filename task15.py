class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name):
        if name not in self.tasks:
            self.tasks.append(name)

    def show_tasks(self):
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i]}")
            

todo = TodoList()
todo.add_task("Do homework")
todo.add_task("Clean room")
todo.add_task("do Lessons")
todo.add_task("Clean room")
todo.show_tasks()