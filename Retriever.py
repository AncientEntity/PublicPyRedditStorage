import praw
import config
import Debug
import EncodeDecoder
import time

reddit = praw.Reddit(username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent="linux:PyRedditStorageRetriever:v1.0 (by /u/"+config.username+")")

storageSub = reddit.subreddit(config.storageSubreddit)


Debug.Log("Retriever Module has been initialized.")


def LocateFilePostByName(fileName):
    postsCreatedFile = open("postsCreated.dat","r+")
    postIDs = postsCreatedFile.read().split("\n")
    postsCreatedFile.close()
    for id in postIDs:
        if(id == ""):
            continue
        if(id.split("|")[1] == fileName):
            return reddit.submission(id.split("|")[0])
    return None

def RetrieveFile(fileName):
    Debug.Log("Searching for file's post.")
    identifiedSubmission = LocateFilePostByName(fileName)
    if(identifiedSubmission == None):
        Debug.Log("Couldn't identify file's post. Perhaps it wasn't ever uploaded?")
        return -1
    else:
        Debug.Log("Found file's post. URL: "+identifiedSubmission.url)
    downloadedFileData = ""
    allComments = identifiedSubmission.comments
    topLevelComment = None
    for comment in allComments:
        if("t3_" in comment.parent_id[:3]):
            topLevelComment = comment
            break
    lastComment = topLevelComment
    searching = True
    commentIndex = 0
    while(searching):
        downloadedFileData = downloadedFileData + lastComment.body
        if(len(lastComment.replies) == 0):
            searching = False
        else:
            if(isinstance(lastComment.replies[0],praw.models.MoreComments)):
                lastComment = lastComment.replies[0].comments()[0]
            else:
                lastComment = lastComment.replies[0]
        Debug.Log("Collected file segment("+str(commentIndex)+")")
        commentIndex+=1
    Debug.Log("All file data retrieved. Beginning decoding")
    decodedData = EncodeDecoder.DecodeFileData(downloadedFileData)
    Debug.Log("Cleaning up special characters")
    #decodedData.replace("\\n","\n")
    #decodedData.replace("\\t","\t")
    #decodedData.replace("\\'","\'")
    #decodedData.replace("\\\"","\"")
    return decodedData
