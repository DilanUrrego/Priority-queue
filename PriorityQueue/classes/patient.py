class Patient:
    def __init__(self, name: str, age: int, description: str, priority: int):
        self.name = name
        self.age = age
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.name} is {self.age} years old with a priority of {self.priority}\n Description: {self.description}"
        