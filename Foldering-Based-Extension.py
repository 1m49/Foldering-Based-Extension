import glob
import os


files_list = glob.glob('*')

# Use set to prevent duplicate file extensions
extension_list = set()

# Extracting file extensions 
for filename in files_list:
    try:
        extension = filename.split('.')[1]
        extension_list.add(extension)
    except:
        continue


# creating folders based on file extensions
def create_folder():
    for ext in extension_list:
        try:
            os.makedirs(ext + '-files')
        except:
            continue


# Transfer files to the folder associated with their file extensionّ
def move_files():
    for each_file in files_list:
        try:
            extension = each_file.split('.')[1]
        # rename > for routing files | gives 2 argumant (src,dst) | src : means from and dst : means : to
            os.rename(each_file, extension+'-files/'+each_file)
        except:
            continue


create_folder()
move_files()
