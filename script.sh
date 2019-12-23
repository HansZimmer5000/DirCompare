#!/usr/bin/env sh

print_help() {
  cat<<EOF

This script compares two folders with the same (subfolder) structure, the first folder is the 'older' folder version, the second folder is the 'newer' folder version. Any folders or files that are new / updated / missing in the older version will be returned by this function. 

The algorithm first compares the diferent folder sizes, if it's not equal, this will be repeated until all folders have been checked. If the folders are unequal but its subfolder (if there are any) are equal, then the files are compared and difference will be returned. In total all differences in files will be returned. To this point, folder differences are considered as differences of their files.

Usage: ./script.sh path/to/older/folderversion path/to/newer/folderversion
EOF
}

get_only_folder_size() {
  ls $1 -l --block-size=1 | head -n 1 | cut -f 2 -d ' '
}

get_complete_folder_size() {
  du -c $1 -b | tail -n 1 | cut -f 1 
}

print_file_differences() {
  echo "NIY print_file_differences"
}

compare_folders() {
  first_size=$(get_complete_folder_size "$1" | tail -n 1)
  second_size=$(get_complete_folder_size "$2" | tail -n 1)

  echo "Have First ($first_size) and Second ($second_size)"
  if [ $first_size -eq $second_size ]; then
    # Nothing to do
    echo "all fine"
  else 
    # Updated Files are maybe in this folder or its subfolders
    echo "not fine"
    first_size=$(get_only_folder_size "$1" | tail -n 1)
    second_size=$(get_only_folder_size "$2" | tail -n 1)
    echo "Have First ($first_size) and Second ($second_size)"
    if [ $first_size -eq $second_size ]; then
      # Updated Files are only in subfolders
      echo "all fine"
    else 
      # Updated Files are in this folder and maybe in subfolders too.
      echo "not fine"
    fi

    # TODO get subfolders for both folders and continue synchronised (same subfolders at the same time.)
  fi
}

# TODO refactor input checks
# TODO test if input is also valid directory.
if [ -z $1 ]; then
  print_help
elif [ -z $2 ]; then
  print_help
elif [ $# -le 1 ]; then
  print_help
else 
  compare_folders $1 $2
fi
