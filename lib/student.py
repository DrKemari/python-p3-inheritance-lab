from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # inherit first_name, last_name
        self.knowledge = []  # start with an empty knowledge list

    def learn(self, info):
        self.knowledge.append(info)  # add new knowledge string
