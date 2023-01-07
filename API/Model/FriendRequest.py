from .Photo import Photo
from .User import User

class FriendSuggestion(object):
    def __init__(self, data):
        self.m_user = User(data)
        self.m_fullName = data["fullname"]
        self.m_mutualFriends = data["mutualFriends"]

        self.m_profilePhoto = data.get("profilePicture", None) # Some users can have no profile picture
        if self.m_profilePhoto is not None:
            self.m_profilePhoto = Photo(self.m_profilePhoto)

    def __repr__(self) -> str:
        return f"<FriendSuggestion {self.m_user.m_username}, mutual friends: {self.m_mutualFriends})>"   

class FriendRequest(FriendSuggestion):
    def __init__(self, data):
        super().__init__(data)

        self.m_status = data["status"]

    def __repr__(self) -> str:
        return f"<FriendRequest {self.m_user.m_username}, status: {self.m_status})>"


         