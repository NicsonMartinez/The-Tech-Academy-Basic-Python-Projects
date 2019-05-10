# DRILL:
# Drill Description:
# For this drill, you will need to write a script that will check a specific folder on the hard drive,
# verify whether those files end with a “.txt” file extension and if they do, print those qualifying
# file names and their corresponding modified time-stamps to the console.
#
# By: Nicson Martinez
# Date: 5/9/2019

import os
from datetime import datetime

# Here I am listing 
fPath = 'C:\\test-directory\\'
directoryList = os.listdir(fPath) 
print("These are the files in the path, C:\\test-directory\\ :\n\n{}\n\n".format(directoryList))

#This finds the 
txtFilesList = []
for i in directoryList:
    if i.endswith('.txt'):
        txtFilesList.append(i)
print("Here is a list of only files that end in '.txt' :\n\n{}\n\n".format(txtFilesList))

pathsList = []
for i in txtFilesList:
    abPath = os.path.join(fPath, i)
    pathsList.append(abPath)

file1 = pathsList[0]
time1 = os.path.getmtime(pathsList[0])
file1Time = datetime.fromtimestamp(time1).strftime('%Y-%m-%d %H:%M:%S')

file2 = pathsList[1]
time2 = os.path.getmtime(pathsList[1])
file2Time = datetime.fromtimestamp(time2).strftime('%Y-%m-%d %H:%M:%S')

print("The following includes the absolute path of each file found and the \ndate & time that each file was last modified: \n")

print("1. {}: {}\n2. {} : {}\n".format(file1,file1Time,file2,file2Time))

