#!python

def dash():
    print("="*32)

# enrich path list;
path_list = [r"D:\04_docu",r"D:\05_file\MATLAB", r"D:\SVN\NexteV_EAC\EAC_IDS\Mulecar\sw"]

# change the list to dict;
path_dict = {}
for i,path in enumerate(path_list):
    path_dict[i] = path

dash()
print("All paths are here:")
dash()
for key,value in path_dict.items():
    print(key,":",value)
dash()

# get dict value base one input key;
index = input("\nChoose one path:\n")
try:
    index = int(index)
except BaseException:
    index = 0

target_path = ""
if index in path_dict:
    target_path = path_dict[index]
else:
    target_path = path_dict[0]
dash()

# open the right path;
command = r"start " + target_path
print(command, "...")

import os
os.system(command)