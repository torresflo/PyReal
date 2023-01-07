import pendulum

from .RealMoji import RealMoji
from .Photo import Photo
from .Device import Device

class User(object):
    def __init__(self, data):
        self.m_data = data
        self.m_id = data["id"]
        self.m_username = data["username"]

    def __repr__(self) -> str:
        return f"<User {self.m_username}>"   

class ConfidentialUser(User):
    def __init__(self, data):
        super().__init__(data)

        self.m_fullName = data["fullname"]
        self.m_profilePhoto = Photo(data["profilePicture"])
        self.m_birthDate = pendulum.parse(data["birthdate"])
        self.m_realMojis = []
        for realMojiData in data["realmojis"]:
            self.m_realMojis.append(RealMoji(realMojiData))
        self.m_devices = []
        for deviceData in data["devices"]:
            self.m_devices.append(Device(deviceData))
        self.stats = data["stats"]
        self.m_phoneNumber = data["phoneNumber"]
        self.m_biography = data["biography"]
        self.m_location = data["location"]
        self.m_countryCode = data["countryCode"]
        self.m_region = data["region"]
        self.m_createdAt = pendulum.parse(data["createdAt"])

    def __repr__(self) -> str:
        return f"<ConfidentialUser {self.m_username} ({self.m_fullName})>"
