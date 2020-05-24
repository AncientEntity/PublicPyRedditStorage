import praw
import config
import Debug
import EncodeDecoder
import time

reddit = praw.Reddit(username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent="linux:PyRedditStorageUpload:v1.0 (by /u/"+config.username+")")

storageSub = reddit.subreddit(config.storageSubreddit)


Debug.Log("Uploader Module has been initialized.")


def UploadFile(fileDirectory):
    Debug.Log(" Beginning upload of file: "+fileDirectory)
    #First create an encoded file map with base 64
    fileToBeUploaded = open(fileDirectory,"rb")
    fileContents = fileToBeUploaded.read()
    fileName = fileDirectory.replace("/","\\").split("\\")[len(fileDirectory.replace("/","\\").split("\\"))-1]
    Debug.Log("File name identified: "+fileName)
    fileToBeUploaded.close()
    encodedData = EncodeDecoder.EncodeAndSeparate(fileContents)
    #print(encodedData)
    Debug.Log("File information encoded & segmented. Creating master reddit thread.")
    masterPost = storageSub.submit(title=fileName,selftext=fileName)
    lastReply = masterPost
    segmentIndex = 1
    for segment in encodedData:
        #print(segment)
        lastReply = lastReply.reply(segment)
        Debug.Log("Segment("+str(segmentIndex)+"/"+str(len(encodedData))+") has been uploaded.")
        #time.sleep(0.1)
        segmentIndex += 1
    Debug.Log("All segments uploaded.")
    Debug.Log("Upload Finished")
    postsCreated = open("postsCreated.dat","a")
    postsCreated.write(masterPost.id+"|"+fileName+"\n")
    postsCreated.close()
    Debug.Log("Added post ID to postsCreated.dat")