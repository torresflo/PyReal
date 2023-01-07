import pendulum

class RealMoji(object):
    def __init__(self, data):
        self.m_data = data
        self.m_emoji = data["emoji"]

        if "uri" in data:
            self.m_photoUrl = data["uri"]
        else:
            self.m_photoUrl = data["media"]["url"]

    def __repr__(self) -> str:
        return f"<RealMoji {self.m_emoji}>"

class PostedRealMoji(RealMoji):
    def __init__(self, data):
        super().__init__(data)

        self.m_date = pendulum.from_timestamp(data["date"]["_seconds"])
        self.m_type = data["type"]
        self.m_username = data["userName"]
        from .User import User
        self.m_user = User(data["user"])

    def __repr__(self) -> str:
        return f"<PostedRealMoji {self.m_emoji} by {self.m_user} on {self.m_date}>"

