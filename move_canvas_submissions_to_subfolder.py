import os
import shutil

directory = "."
delim = "_"

contents = os.listdir(directory)
#create directory
for item in contents:
    if(os.path.isdir(item)):
        continue
    parts = item.split(delim)
    folder = parts[0]
    if not os.path.exists(os.path.join(directory,folder)):
        os.mkdir(folder)
    if not "LATE" in item:
        filename = "_".join(parts[3:])
    else:
        filename = "_".join(parts[4:])
    print("src: " + str(os.path.join(directory, item)))
    print("dest: " + str(os.path.join(directory, folder, filename)))
    shutil.copyfile(
        os.path.join(directory, item),
        os.path.join(directory, folder, filename)
    )
    
