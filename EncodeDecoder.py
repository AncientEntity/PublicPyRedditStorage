import base64
import config


def EncodeAndSeparate(fileData):
    encodedData = str(base64.b64encode(fileData))
    encodedData = encodedData[2:len(encodedData)-1]


    segments = []
    segmentCount = int(len(encodedData)/config.maxCommentSize)+1
    for segmentIndex in range(segmentCount):
        currentSegment = ""
        for char in range(config.maxCommentSize):
            if(char+(segmentIndex*config.maxCommentSize) > len(encodedData)-1):
                break #It hit end of file
            try:
                currentSegment = currentSegment + encodedData[char+(segmentIndex*config.maxCommentSize)]
            except:
                pass
                #print(""+str((char+(segmentIndex*config.maxCommentSize)))+","+str(len(encodedData)))
        segments.append(currentSegment)
    return segments

def DecodeFileData(fileData):
    return base64.b64decode(bytes(fileData,"ascii"))
