import os
import sys
import time
import filecmp

from compare import compare_directories

def input_is_directory(input):
    return os.path.isdir(input)

def get_directories_from_arguments(arguments):
    try:
        if(input_is_directory(arguments[1])):
            dir1 = arguments[1]
        else:
            raise ValueError("Input 1 is not a valid Directory")
        if(input_is_directory(arguments[2])):
            dir2 = arguments[2]
        else:
            raise ValueError("Input 2 is not a valid Directory")
    except IndexError:
        raise IndexError("Not enough Directorienames given")

    return dir1, dir2

if __name__ == "__main__":
    print("Start")
    start_ts = time.time()

    try:
        dir1, dir2 = get_directories_from_arguments(sys.argv)
        dcmp = filecmp.dircmp(dir1, dir2)
        depth = 1
        compare_directories(dcmp, depth)
    except Exception as e:
        print(e)

    end_ts = time.time()
    duration = round(end_ts - start_ts)

    print("End after %s seconds" %(duration))