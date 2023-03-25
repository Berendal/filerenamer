import os
path = '' #folder
files = os.listdir(path)
for file in files:
    # print(file)
    os.rename(os.path.join(path, file), os.path.join(path, file[:6] + file[6:-4].rjust(3, '0') + file[-4:])) #files for rename, how/what change
