import pendulum

from .User import User
from .Comment import Comment
from .RealMoji import PostedRealMoji

class Post(object):
    def __init__(self, data):
        self.m_data = data
        self.m_id = data["id"]
        self.m_notificationId = data["notificationID"]
        self.m_ownerId = data["ownerID"]
        self.m_username = data["userName"]
        self.m_user = User(data["user"])
        self.m_mediaType = data["mediaType"]
        self.m_region = data["region"]
        self.m_bucket = data["bucket"]
        self.m_primaryPhotoUrl = data["photoURL"]
        self.m_secondaryPhotoUrl = data["secondaryPhotoURL"]
        self.m_lateInSeconds = data["lateInSeconds"]
        self.m_isPublic = data["isPublic"]
        self.m_location = data.get("location", None)
        self.m_retakeCounter = data["retakeCounter"]
        self.m_creationDate = pendulum.from_timestamp(data["creationDate"]["_seconds"])
        self.m_updatedAt = pendulum.from_timestamp(data["updatedAt"] / 1000)
        self.m_comments = []
        for commentData in data["comment"]:
            self.m_comments.append(Comment(commentData))
        self.m_realMojis = []
        for realMojiData in data["realMojis"]:
            self.m_realMojis.append(PostedRealMoji(realMojiData))
        
    def __repr__(self) -> str:
        return f"<Post {self.m_id} by {self.m_username}>"
