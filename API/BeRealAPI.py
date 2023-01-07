import requests
import pendulum
import hashlib

from Utils.DataTools import DataSaver

from .Model.User import User, ConfidentialUser
from .Model.Post import Post
from .Model.FriendRequest import FriendSuggestion, FriendRequest
from .Model.Memory import Memory

class BeRealConnectionHandler:
    def __init__(self):
        self.m_googleApiKey = "AIzaSyDwjfEeparokD7sXPVQli9NsTuhT6fJ6iA"

    def __repr__(self) -> str:
        return f"<BeRealConnectionHandler (token={self.m_token})>"

    def connect(self, phoneNumber: str) -> None:
        self.loadRefreshToken()
        if self.m_refreshToken:
            self.refreshTokens()
            self.saveRefreshToken()
            print("Token loaded from file and refreshed.")
        else:
            self.sendOTP(phoneNumber)
            otp = input("Enter OTP: ")
            self.verifyOTP(otp)
            self.saveRefreshToken()
            print("Token received with OTP and saved in file.")

    def sendOTP(self, phoneNumber: str):
        result = requests.post(
            "https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode",
            params={"key": self.m_googleApiKey},
            data={
                "phoneNumber": phoneNumber,
                "iosReceipt": "AEFDNu9QZBdycrEZ8bM_2-Ei5kn6XNrxHplCLx2HYOoJAWx-uSYzMldf66-gI1vOzqxfuT4uJeMXdreGJP5V1pNen_IKJVED3EdKl0ldUyYJflW5rDVjaQiXpN0Zu2BNc1c",
                "iosSecret": "KKwuB8YqwuM3ku0z",
            },
            headers={
                "x-firebase-client": "apple-platform/ios apple-sdk/19F64 appstore/true deploy/cocoapods device/iPhone9,1 fire-abt/8.15.0 fire-analytics/8.15.0 fire-auth/8.15.0 fire-db/8.15.0 fire-dl/8.15.0 fire-fcm/8.15.0 fire-fiam/8.15.0 fire-fst/8.15.0 fire-fun/8.15.0 fire-install/8.15.0 fire-ios/8.15.0 fire-perf/8.15.0 fire-rc/8.15.0 fire-str/8.15.0 firebase-crashlytics/8.15.0 os-version/14.7.1 xcode/13F100",
                "user-agent":"FirebaseAuth.iOS/8.15.0 AlexisBarreyat.BeReal/0.22.4 iPhone/14.7.1 hw/iPhone9_1",
                "x-ios-bundle-identifier": "AlexisBarreyat.BeReal",
                "x-firebase-client-log-type": "0",
                "x-client-version": "iOS/FirebaseSDK/8.15.0/FirebaseCore-iOS",
            }
        ).json()

        if "error" in result:
            raise Exception("Error when sending the OTP request. Probably the quota is exceeded, try again.")
        
        self.m_otpSession = result["sessionInfo"]

    def verifyOTP(self, otp: str):
        if self.m_otpSession is None:
            raise Exception("No open OTP session")
        result = requests.post(
            "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPhoneNumber",
            params={"key": self.m_googleApiKey},
            data={
                "sessionInfo": self.m_otpSession,
                "code": otp,
                "operation": "SIGN_UP_OR_IN",
            },
        ).json()

        if "error" in result:
            raise Exception("Error when verifying the OTP. Probably the quota is exceeded, try again.")

        self.m_token = result["idToken"]
        self.m_refreshToken = result["refreshToken"]
        self.m_expiration = pendulum.now().add(seconds=int(result["expiresIn"]))
        self.m_userId = result["localId"]

    def saveRefreshToken(self):
        if self.m_token is None:
            raise Exception("No token found. Are you connected?")
        DataSaver.saveTokenInFile(self.m_refreshToken)

    def loadRefreshToken(self):
        self.m_refreshToken = DataSaver.readTokenFromFile()

    def refreshTokens(self):
        if self.m_refreshToken is None:
            raise Exception("No refresh token.")
        result = requests.post(
            "https://securetoken.googleapis.com/v1/token",
            params={"key": self.m_googleApiKey},
            data={
                "refresh_token": self.m_refreshToken,
                "grant_type": "refresh_token"
            },
        ).json()

        self.m_token = result["id_token"]
        self.m_refreshToken = result["refresh_token"]
        self.m_expiration = pendulum.now().add(seconds=int(result["expires_in"]))
        self.m_userId = result["user_id"]

class PyReal:
    def __init__(self):
        self.m_beRealConnection = BeRealConnectionHandler()
        self.m_beRealApiUrl = "https://mobile.bereal.com/api"

    def isConnected(self):
        return self.m_beRealConnection.m_token is not None

    def connect(self, phoneNumber: str):
        self.m_beRealConnection.connect(phoneNumber)

    def getUserInfo(self):
        if self.isConnected():
            result = requests.get(
                f"{self.m_beRealApiUrl}/person/me",
                headers={
                    "authorization": self.m_beRealConnection.m_token
                },
            ).json()
            return ConfidentialUser(result)

    def getUserList(self, url):
        if self.isConnected():
            result = requests.get(
                url,
                headers={
                    "authorization": self.m_beRealConnection.m_token
                },
            ).json()
            return result["data"]

    def getFriends(self):
        users = self.getUserList(f"{self.m_beRealApiUrl}/relationships/friends")
        return self.parseUserList(users)

    def getFriendSuggestions(self):
        suggestions = self.getUserList(f"{self.m_beRealApiUrl}/relationships/suggestions")
        friendSuggestions = []
        for friendSuggestion in suggestions:
            friendSuggestions.append(FriendSuggestion(friendSuggestion))
        return friendSuggestions

    def getFriendRequests(self, requestType):
        requests = self.getUserList(f"{self.m_beRealApiUrl}/relationships/friend-requests/{requestType}")
        friendRequests = []
        for request in requests:
            friendRequests.append(FriendRequest(request))
        return friendRequests

    def getSentFriendRequests(self):
        return self.getFriendRequests("sent")
    
    def getReceivedFriendRequests(self):
        return self.getFriendRequests("received")

    def getMemories(self):
        if self.isConnected():
            result = requests.get(
                f"{self.m_beRealApiUrl}/feeds/memories",
                headers={
                    "authorization": self.m_beRealConnection.m_token
                },
            ).json()

            memories = []
            for memoryData in result["data"]:
                memories.append(Memory(memoryData))
            return memories

    def getFriendsFeed(self):
        if self.isConnected():
            result = requests.get(
                f"{self.m_beRealApiUrl}/feeds/friends",
                headers={
                    "authorization": self.m_beRealConnection.m_token
                },
            ).json()
            return self.parsePostList(result)

    def getDiscoveryFeed(self):
        if self.isConnected():
            result = requests.get(
                f"{self.m_beRealApiUrl}/feeds/discovery",
                headers={
                    "authorization": self.m_beRealConnection.m_token
                },
            ).json()
            return self.parsePostList(result["posts"])

    def parseUserList(self, usersData):
        users = []
        for userData in usersData:
            users.append(User(userData))
        return users

    def parsePostList(self, postsData):
        posts = []
        for postData in postsData:
            posts.append(Post(postData))
        return posts
        