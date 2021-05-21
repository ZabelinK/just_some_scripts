import os
import sys
import codecs

def size_with_suffix(size):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    suffix_idx = 0
    while size > 1024:
        size /= 1024
        suffix_idx += 1
    return "{}{}".format(round(size, 1), suffixes[suffix_idx])

if len(sys.argv) != 2:
    print("Wrong args: {}\nUsage: {} path".format(sys.argv, sys.argv[0]))
    exit(1)

files = []
size_of_all = 0
number_of_files = 0

for (dirpath, dirnames, filenames) in os.walk(sys.argv[1]):
    for file in filenames:
        full_file_path = dirpath + os.path.sep + file
        file_size = os.path.getsize(full_file_path)
        size_of_all += file_size
        files.append(
                     {
                        "path" : full_file_path, 
                        "size" : file_size
                     }
                    )
    number_of_files += len(filenames)
    print("Size: {} Number of files: {}\r".format(size_with_suffix(size_of_all), number_of_files), end='')

print("Size: {} Number of files: {}\nSorting files by size...".format(size_with_suffix(size_of_all), number_of_files))

files = sorted(files, key=lambda file: file["size"], reverse=True)
with codecs.open('out.txt', 'w', 'utf-8') as f:
    for file in files:
        f.write("{} {}\n".format(size_with_suffix(file["size"]), file["path"]))
