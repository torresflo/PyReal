import os
import io
import requests

from PIL import Image

class DataSaver:
    DefaultSavePath = "./saved"
    DefaultPhotoSavePath = f"{DefaultSavePath}/photos"
    DefaultRefreshTokenFileName = f"{DefaultSavePath}/token.txt"

    def createFolder(folderName):
        if not os.path.isdir(folderName):
            os.makedirs(folderName, exist_ok=True)

    def saveTokenInFile(token: str):
        DataSaver.createFolder(DataSaver.DefaultSavePath)
        with open(DataSaver.DefaultRefreshTokenFileName, "w+", encoding="utf-8") as file:
            file.write(token)

    def readTokenFromFile():
        if not os.path.exists(DataSaver.DefaultRefreshTokenFileName):
            return None
        with open(DataSaver.DefaultRefreshTokenFileName, "r", encoding="utf-8") as file:
            return file.read()

    def saveImage(image : Image, fileName: str):
        DataSaver.createFolder(DataSaver.DefaultPhotoSavePath)
        image.save(f"{DataSaver.DefaultPhotoSavePath}/{fileName}.jpg")

class DataDownloader:
    def downloadImage(url: str):
        result = requests.get(url)
        image = Image.open(io.BytesIO(result.content))
        image.convert("RGB")
        return image

class DataModifier:
    def combineImages(leftImage: Image, rightImage: Image):
        combinedImage = Image.new("RGB", (2 * leftImage.width, leftImage.height))
        combinedImage.paste(leftImage, (0,0))
        combinedImage.paste(rightImage, (leftImage.width, 0))
        return combinedImage