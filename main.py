import sys
import dirTree

def gather_arguments(arguments):
    if(len(arguments) > 2):
        if(len(arguments) > 3):
            depth = int(arguments[3])
        else:
            depth = 2

        startfolderFullPath1 = arguments[1]
        startfolderFullPath2 = arguments[2]
        result = (startfolderFullPath1, startfolderFullPath2, depth)
    else:
        result = None

    return result

if __name__ == "__main__":
    arguments = gather_arguments(sys.argv)

    if(arguments is None):
        print("To less / wrong arguments")

    else:
        startfolderFullPath1, startfolderFullPath2, depth = arguments

        dirTree1 = dirTree.Create_dir_tree(startfolderFullPath1, depth)
        dirTree2 = dirTree.Create_dir_tree(startfolderFullPath2, depth)
        print(dirTree1)
        print(dirTree2)
        dirTree.Compare_dir_tree(dirTree1, dirTree2)        
