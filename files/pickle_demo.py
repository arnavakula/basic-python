class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    
    def display(self):
        print(self.id)
        print(self.name)
        print(self.score)
