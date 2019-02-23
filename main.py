import sys
import os

def calculateDirSizeInMb(dirFullPath):
    size = 0
    for (path, _, files) in os.walk(dirFullPath):
        for file in files:
            filename = os.path.join(path,file)
            size += os.path.getsize(filename)
    return round(size / (1024*1024), 2)

def dirContainsSubDirs(directory):
    for element in os.listdir(directory):
        if(os.path.isdir(directory + "/" + element)):
            return True
    
    return False

def createDirTree(startfolderFullPath, depth):
    if(depth >= 0):
        if(dirContainsSubDirs(startfolderFullPath)):
            size = calculateDirSizeInMb(startfolderFullPath)
            date = None
            subDirs = {}
            for element in os.listdir(startfolderFullPath):
                if(os.path.isdir(startfolderFullPath + "/" + element)):
                    tmpSubdir = createDirTree(startfolderFullPath + "/" + element, depth - 1)
                    subDirs = {**subDirs, **tmpSubdir}
            return {startfolderFullPath: (size,date ,subDirs)}
        else:
            size = calculateDirSizeInMb(startfolderFullPath)
            date = None
            subDirs = {}
            return {startfolderFullPath: (size, date, subDirs)}
    else:
        return {}


if __name__ == "__main__":
    arguments = sys.argv

    if(len(arguments) > 2):
        if(len(arguments) > 3):
            depth = int(arguments[3])
        else:
            depth = 2

        startfolderFullPath1 = arguments[1]
        startfolderFullPath2 = arguments[2]
        dirTree1 = createDirTree(startfolderFullPath1, depth)
        dirTree2 = createDirTree(startfolderFullPath2, depth)
        print(dirTree1)
        print(dirTree2)
    else:
        print("Not two Startfolders given!")