import os

def calc_dirsize_mb(dirFullPath):
    size = 0
    for (path, _, files) in os.walk(dirFullPath):
        for file in files:
            filename = os.path.join(path,file)
            size += os.path.getsize(filename)
    return round(size / (1024*1024), 2)

def dir_contains_subdirs(directory):
    for element in os.listdir(directory):
        if(os.path.isdir(directory + "/" + element)):
            return True
    
    return False

def get_root_and_current_folder(full_path):
    path, folder_name = os.path.split(full_path)
    return path, folder_name

def combine_dirtree_keys(dictionaryList):
    keySet = set([])
    for dictionary in dictionaryList:
        if(isinstance(dictionary, dict)):
            for key in dictionary:
                root, folder_name = get_root_and_current_folder(key)
                #TODO: What todo with root?
                keySet.add(folder_name)

    return keySet

def all_dictionaries_contains_key(dictionaryList, key):
    result = True
    
    if(len(dictionaryList) > 0):
        for dictionary in dictionaryList:
            if(isinstance(dictionary, dict)):
                try:
                    dictionary[key]
                except KeyError:
                    result = False
            else:
                result = False
    else:
        result = False
    
    return result

def compare_files(files1, files2):
    union = filter(lambda x: x in files1, files2)
    only_files1 = filter(lambda x: x in files1 and x not in files2)
    only_files2 = filter(lambda x: x in files2 and x not in files1)

    print(union)
    print(only_files1)
    print(only_files2)

def compare_files_in_dirs(dir1, dir2):
    dir_files1 = os.listdir(dir1)
    dir_files2 = os.listdir(dir2)
    compare_files(dir_files1, dir_files2)

def compare_subdir_tree(dirTree1, dirTree2):
    keySet = combine_dirtree_keys([dirTree1, dirTree2])
    for key in keySet:
        if(all_dictionaries_contains_key([dirTree1, dirTree2], key)):
            (size1, date1, subdirs1) = dirTree1[key]
            (size2, date2, subdirs2) = dirTree2[key]
            #compare_files_in_dirs(key)

            if((size1 != size2) or (date1 != date2)):
                print("Metadata Wrong: " + key)

            compare_subdir_tree(subdirs1, subdirs2)
        else:
            print("Only in One Dir: " + key)

########################################

def Create_dir_tree(startfolderFullPath, depth):
    if(depth >= 0):
        if(dir_contains_subdirs(startfolderFullPath)):
            size = calc_dirsize_mb(startfolderFullPath)
            date = None
            subDirs = {}
            for element in os.listdir(startfolderFullPath):
                if(os.path.isdir(startfolderFullPath + "/" + element)):
                    tmpSubdir = Create_dir_tree(startfolderFullPath + "/" + element, depth - 1)
                    subDirs = {**subDirs, **tmpSubdir}
            return {startfolderFullPath: (size,date ,subDirs)}
        else:
            size = calc_dirsize_mb(startfolderFullPath)
            date = None
            subDirs = {}
            return {startfolderFullPath: (size, date, subDirs)}
    else:
        return {}

def Compare_dir_tree(dirTree1, dirTree2):
    for key in dirTree1:
        (size1, date1, subdirs1) = dirTree1[key]

    for key in dirTree2:
        (size2, date2, subdirs2) = dirTree2[key]

    if((size1 != size2) or (date1 != date2)):
        print("Metadata Wrong: " + key)

    compare_subdir_tree(subdirs1, subdirs2)
