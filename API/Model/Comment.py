from .User import User

class Comment(object):
    def __init__(self, data):
        self.m_data = data
        self.m_id = data["id"]
        self.m_text = data["text"]
        self.m_creationDate = data["creationDate"]
        self.m_user = User(data["user"])

    def __repr__(self) -> str:
        return f"<Comment {self.m_id} by {self.m_user.m_username}"
    

