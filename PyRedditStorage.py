import praw
import time
import Debug
import config
import Uploader
import Retriever
import os
currentDirectory = os.path.dirname(os.path.abspath(__file__))

Debug.Log("PyRedditStorage Loaded.")

def UploadFile(fileDirectoryAndName):
    Uploader.UploadFile(fileDirectoryAndName)

def RetrieveFileAndSave(fileName,fileSaveLocation=currentDirectory,overrideName=""):
    data = Retriever.RetrieveFile(fileName)
    if(overrideName != ""):
        fileName = overrideName
    if(data == -1):
        raise("Exception: Retriever returned -1. Most likely file couldn't be found.")
    Debug.Log("Saving file.")
    saveFile = open(fileSaveLocation + "\\" + fileName, "wb")
    saveFile.write(data)
    saveFile.close()
    Debug.Log("File saved. Retrieval complete.")
