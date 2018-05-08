# what this script does:
# given a folder, traverse it, find the startTime logged in "*.inf" file, and append to its containing folder;
import os,re

# placeholder for medium variabls;
sourceDirList = [] # directory list
labelList = [] # label list
targetDirList = [] # target directory list
targetDirDic = {}

# store old target directories;
basePath = os.getcwd()
for item in os.listdir("."):
    if os.path.isdir(item) and re.search(r"\.",item) == None:
        dirPath = os.path.join(basePath,item)
        sourceDirList.append(dirPath)

# in interested directories, find *.inf and parse it;
for dd in sourceDirList:
    for item in os.listdir(dd):
        label = ""
        if re.search("inf",item) != None:
            itemPath = os.path.join(dd,item)
            f = open(itemPath)
            for line in f.readlines():
                if re.search(r"startTime", line) != None:
                    time = re.search(r"(?<=\s)\d{2}:.*$", line)
                    if time != None:
                        label = time.group()
                        labelList.append(label)
                    break
            f.close()

# replace ":" with "_" because Windows won't allow file name with ":"
for i,label in enumerate(labelList):
    newTimeFormat = re.sub(r":",r"_",label)
#     newTimeFormat = re.sub(r"\s",r"",newTimeFormat)
    labelList[i] = newTimeFormat

# replace names;
for i,item in enumerate(sourceDirList):
    newName = item + "_" + labelList[i]
    try:
        os.rename(item,newName)
    except OSError as e:
        print(e)
        