import os
import sys

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_complete(self, index):
        if index >= 0 and index < len(self.tasks):
            self.tasks[index] = self.tasks[index] + " (done)"

    def print_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def run_command(self, command):
        if command[0] == "a":
            # add a task
            task = " ".join(command[1:])
            self.add_task(task)
        elif command[0] == "r" and len(command) > 1:
            # remove a task
            index = int(command[1]) - 1
            self.remove_task(index)
        elif command[0] == "c" and len(command) > 1:
            # mark a task as complete
            index = int(command[1]) - 1
            self.mark_task_complete(index)
        elif command[0] == "p":
            # print the tasks
            self.print_tasks()
        else:
            print("Unrecognized command")

    def start(self):
        while True:
            # read a command
            command = input("Enter command: ").split()
            self.run_command(command)

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.start()
