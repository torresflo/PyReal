class Device(object):
    def __init__(self, data):
        self.m_data = data
        self.m_clientVersion = data["clientVersion"]
        self.m_deviceName = data["device"]
        self.m_deviceId = data["deviceId"]
        self.m_pushToken = data["pushToken"]
        self.m_platform = data["platform"]
        self.m_language = data["language"]
        self.m_timezone = data["timezone"]

    def __repr__(self) -> str:
        return f"<Device {self.m_deviceName}>"