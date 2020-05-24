from tkinter import *
import tkinter.filedialog
import PyRedditStorage
import Debug

window = Tk()
window.title("PyRedditStorage GUI")
window.configure(background="white")
title = Label(window,text="Python Reddit Storage GUI",fg="black",font="none 12 bold",bg="white")
title.grid(row=1,column=0,pady=(25,40))

pickedFile = ""
selected = False

def GetAllFilesUploaded():
    postsCreated = open("postsCreated.dat","r+")
    postList = postsCreated.read().split("\n")
    postNames = []
    for post in postList[0:len(postList)-1]:
        #print(post)
        postNames.append(post.split("|")[1])
    return postNames

def PopupMessage(title,msg):
    popup = Tk()
    popup.title(title)
    label = Label(popup,text=msg,font="none 12 bold")
    label.pack(side="top",fill="x",pady=10)
    B1 = Button(popup,text="Okay",command=popup.destroy)
    B1.pack()
    popup.mainloop()

def DoSelected():
    global selected
    selected = True

def GetFileList(title,msg):
    global pickedFile, selected
    popup = Tk()
    popup.title(title)
    label = Label(popup,text=msg,font="none 12 bold")
    label.pack(side="top",fill="x",pady=10)
    label.grid(row=1,column=0)
    allFiles = GetAllFilesUploaded()
    pickedFile = StringVar(popup)
    pickedFile.set(allFiles[0])
    selected = False
    index = 2

    for text in GetAllFilesUploaded():
        radioButton = Radiobutton(popup,text=text,value=text,variable=pickedFile,command=pickedFile.set(text),width=100)
        #radioButton.pack(anchor=W)
        radioButton.grid(row=index,column=0)
        index += 1
    selectButton = Button(popup,text="Select File",command=DoSelected)
    selectButton.grid(row=index,column=0)
    while True:
        popup.update()
        #print(pickedFile.get())
        if(selected == True):
            popup.destroy()
            return pickedFile.get()

def PostCommand():
    fileDirectoryAndName = tkinter.filedialog.askopenfilename()
    if(fileDirectoryAndName == ""):
        PopupMessage("Post Request", "Failed to get file directory and name")
        return
    fileName = fileDirectoryAndName.split("\\")[len(fileDirectoryAndName.split("\\"))-1]
    PyRedditStorage.UploadFile(fileDirectoryAndName)
    PopupMessage("Post Request","Successfully uploaded file: "+fileName)

def GetCommand():
    fileNameToGrab = GetFileList("Get Request","Uploaded Files")
    fileSaveLocation = tkinter.filedialog.asksaveasfilename(filetypes=[('All Files', '*.*')],initialfile=fileNameToGrab)
    directorySplit = fileSaveLocation.split('/')
    finalName = directorySplit[len(directorySplit)-1]
    Debug.Log("File Split Directories: "+str(directorySplit))
    finalDirectory = "\\".join(directorySplit[0:len(directorySplit)-1])
    Debug.Log("Final Directory: "+finalDirectory)
    PyRedditStorage.RetrieveFileAndSave(fileNameToGrab,finalDirectory,overrideName=finalName)


postButton = Button(window,text="Post",width=4,command=PostCommand).grid(row=2,column=0,pady=(0,20))
getButton = Button(window,text="Get",width=4,command=GetCommand).grid(row=3,column=0,pady=(0,25))

window.resizable(False,False)

window.mainloop()
