class Task:
    def __init__(self, id, title, description, isCompleted=False):
        self.id = id
        self.title = title
        self.description = description
        self.isCompleted = isCompleted

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "isCompleted" : self.isCompleted
        }