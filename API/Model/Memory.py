from .Photo import Photo

class Memory(object):
    def __init__(self, data):
        self.m_data = data
        self.m_id = data["id"]
        self.m_thumbnail = Photo(data["thumbnail"])
        self.m_primaryPhoto = Photo(data["primary"])
        self.m_secondaryPhoto = Photo(data["secondary"])
        self.m_isLate = data["isLate"]
        self.m_memoryDay = data["memoryDay"]

    def __repr__(self):
        return f"<Memory {self.m_id}>"