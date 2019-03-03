import os
import filecmp

files_to_be_ignored = [".gitignore"]
directories_to_be_ignored = ["System Volume Information", ".Trash-", "%RECYCLE.BIN"]

def get_files(folder):
    files = set()
    elements = os.listdir(folder)
    
    for element in elements:
        if(os.path.isfile(element)):
            files.add(element)

    return files

def get_dir_size_kb(dir_path):
    size = 0

    for elem_name in os.listdir(dir_path):
        elem_path = "%s/%s" %(dir_path, elem_name)
        try:
            if(os.path.isfile(elem_path)):
                size += get_file_size(elem_path)
            elif (os.path.isdir(elem_path)):
                size += get_dir_size_kb(elem_path)
        except Exception:
            pass

    size_kb = round(size / 1024, 0)
    return size_kb

def get_file_size(file):
    return os.path.getsize(file)

def get_file_change_date(file):
    return os.path.getmtime(file)

def get_common_files(files_names1, files_names2):
    common_files = set()

    for file in files_names1:
        if (file in files_names2) and (file not in files_to_be_ignored):
            common_files.add(file)
    return common_files

def compare_common_files(dcmp):
    files_left = get_files(dcmp.left)
    files_right = get_files(dcmp.right)

    common_files = get_common_files(files_left, files_right)
    for common_file in common_files:
        file_left = "%s/%s" %(dcmp.left, common_file)
        file_right = "%s/%s" %(dcmp.right, common_file)
        
        if(get_file_change_date(file_left) != get_file_change_date(file_right)):
            print("\nDiff Change Time in %s//%s" %(file_left, file_right))
        
        if(get_file_size(file_left) != get_file_size(file_right)):
            print("\nDiff Size in %s//%s" %(file_left, file_right))

def compare_directories(dcmp, depth):
    #Doc: https://docs.python.org/3/library/filecmp.html#filecmp.cmp
    #print("Comparing %s and %s" %(dcmp.left, dcmp.right))
    #print("%s // %s" %(dcmp.left, dcmp.right))

    if(depth > 0):
        for directory_to_be_ignored in directories_to_be_ignored:
            if(directory_to_be_ignored not in dcmp.left) and (directory_to_be_ignored not in dcmp.right):
                dir_size_left = get_dir_size_kb(dcmp.left)
                dir_size_right = get_dir_size_kb(dcmp.right)

                if(dir_size_left != dir_size_right):
                    print("Different Size: %s(%s) // %s(%s) // Diff %s" %(dcmp.left, dir_size_left, dcmp.right, dir_size_right, dir_size_left - dir_size_right))
                
                for name in dcmp.left_only:
                    print("left_only: %s/%s" %(dcmp.left, name))

                for name in dcmp.right_only:
                    print("right_only: %s/%s" %(dcmp.right, name))

                compare_common_files(dcmp)

                for sub_dcmp in dcmp.subdirs.values():
                    compare_directories(sub_dcmp, depth - 1)