from progress.bar import ShadyBar

from API.BeRealAPI import PyReal
from Utils.DataTools import DataDownloader, DataSaver, DataModifier

if __name__ == '__main__':
    print("Please enter your phone number or press Enter if you already have an API Token.")
    phoneNumber = input("Phone number (format: +<country><number>): ")
    
    pyReal = PyReal()
    pyReal.connect(phoneNumber)

    memories = pyReal.getMemories()

    progressBar = ShadyBar("Retrieving memories...", max = len(memories))
    for memory in memories:
        progressBar.next()

        primaryPhoto = DataDownloader.downloadImage(memory.m_primaryPhoto.m_url)
        secondaryPhoto = DataDownloader.downloadImage(memory.m_secondaryPhoto.m_url)
        combinedPhoto = DataModifier.combineImages(secondaryPhoto, primaryPhoto)
        DataSaver.saveImage(combinedPhoto, f"{memory.m_memoryDay}")