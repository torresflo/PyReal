class Photo(object):
    def __init__(self, data):
        self.m_url = data["url"]
        self.m_width = data["width"]
        self.m_height = data["height"]

    def __repr__(self) -> str:
        return f"<Photo {self.url} {self.width}x{self.height}>"