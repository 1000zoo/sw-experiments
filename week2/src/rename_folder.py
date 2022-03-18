import os

path = "/Users/1000zoo/Documents/prog/swExperiment/week2_folder_example"
dir_ = os.listdir(path)
print(dir_)

for folder in dir_:
    temp = folder.split("_")
    rename = temp[1] + "_" + temp[0] + "_rename"
    print(rename)
    os.rename(path + "/" + folder, path + "/" + rename)
dir_ = os.listdir(path)
print(dir_)
