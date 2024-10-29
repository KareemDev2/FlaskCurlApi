from datetime import datetime

class Task:
    def __init__(self, task):
        self.id = None # sera défini lors de l'ajout à la liste
        self.task = task
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
