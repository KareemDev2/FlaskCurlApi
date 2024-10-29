from datetime import datetime

class User:
    def __init__(self, username):
        self.id = None # sera défini lors de l'ajout à la liste
        self.username = username
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
