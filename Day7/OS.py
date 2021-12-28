import os

os.mkdir("Test")

cwd = os.getcwd()
print(cwd)

path = "/"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)

os.rmdir("Test")
