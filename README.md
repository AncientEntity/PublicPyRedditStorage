# PyRedditStorage

## What is this?
######
PythonRedditStorage allows you to store your files on a private subreddit directly on reddit! PythonRedditStorage uses base64 encoding when uploading and decodes it whenever you want to download it. Encryption is coming whenever I feel like it. As well as compression. Reddit comments max out at 10,000 characters (10kbs) so to get around this it'll break up the comments. Upload is roughly 5KB/s estimate while download is roughly 15KB/s estimate, so don't expect storing your computer as a backup on reddit.

## How To

#### Requirements
 - Reddit account (with decent karma so it doesn't get ratelimited too hard)
 - Praw
 - Python3 (Python2 may work but untested)
 
 #### Setup
 0. Install requirements posted above.
 1. Go into config.py and there is some data you must fill in before it will work, the first five variables to be exact. Don't touch any other parameters unless you know what your doing.
 2. Run LaunchGUI.bat or PyRSGUI.py to launch the UI. Take in mind I am not a UI developer so it isn't the best. Another option is to run the methods/functions manually without a UI which I explain below
 
 ### Usage without UI
 So you can't handle my UI? That's alright i'm not a UI developer. There is only two real methods you'll most likely need.
 1. PyRedditStorage.UploadFile(fileDirectoryAndName) explains itself.
 2. PyRedditStorage.RetrieveFileAndSave(fileName,fileSaveLocation,overrideName) -> Only mandatory parameter is fileName, the rest defaults. fileSaveLocation is defaulted to the python file's directory, and overrideName is only there if you want to save it with a different file name as uploaded.
 
 ## Coming Soon Maybe
 1. Encryption
 2. Compression
 3. Better UI (if someone wants to do this one for me that would be great)
 
