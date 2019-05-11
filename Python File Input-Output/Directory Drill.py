# DRILL:
# Drill Description:
# For this drill, you will need to write a script that will check a specific folder on the hard drive,
# verify whether those files end with a “.txt” file extension and if they do, print those qualifying
# file names and their corresponding modified time-stamps to the console.
#
# Requirements:
# Your script will need to use Python 3 and the OS module.
#
# Your script will need to use the listdir() method from the OS module to iterate through all files
# within a specific directory.
# 
# Your script will need to use the path.join() method from the OS module to concatenate the file name to
# its file path, forming an absolute path.
# 
# Your script will need to use the getmtime() method from the OS module to find the latest date that each
# text file has been created or modified.
# 
# Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime
# to the console.
#
# By: Nicson Martinez
# Date: 5/9/2019

import os
from datetime import datetime


fPath = 'C:\\test-directory\\'
directoryList = os.listdir(fPath) #Creates list of files in a specific directory.
print("These are the files in the path, C:\\test-directory\\ :\n\n{}\n\n".format(directoryList))

for file in directoryList:
    if file.endswith('.txt'):
        abPath = os.path.join(fPath, file) #Concatinates the path directory with a txt file found through each iteration. 
        fModTime = os.path.getmtime(abPath) #Gets last modified time.
        formattedTime = datetime.fromtimestamp(fModTime).strftime('%m-%d-%Y %H:%M:%S') #formats the time in a way that humans can understand
        print("File {} : Last-Modified Time {}\n".format(abPath,formattedTime))


