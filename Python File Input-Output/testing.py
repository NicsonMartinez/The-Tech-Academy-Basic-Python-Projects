# DRILL:
# Drill Description:
# For this drill, you will need to write a script that will check a specific folder on the hard drive,
# verify whether those files end with a “.txt” file extension and if they do, print those qualifying
# file names and their corresponding modified time-stamps to the console.

import os

directoryList = os.listdir('C:\\test-directory\\.') 
# Outputs array of files in the current directory (Where this file is stored) when "." is in os.listdir(".")
# Absolute and relative paths can be put into that string value.


print("These are the files in the path, C:\\test-directory\\ :\n\n{}\n\n".format(directoryList))


txtFilesList = []
for i in directoryList:
    if i.endswith('.txt'):
        txtFilesList.append(i)
print("Here is a list of only files that end in '.txt' :\n\n{}\n\n".format(txtFilesList))


fNameList = []
for i in txtFilesList:
    fullFileName = i

    charList = list(fullFileName)   # Converts string into a list of characters

    modCharList = charList[:-4]     # Erases the last four

    fName = ''.join(modCharList)    # Concatinates all of the elements into one string

    fNameList.append(fName)         
        

print(fNameList)


    


##
##fileName = 'Hello.txt'
##
##filePath = 'C:\\A\\' #It can't be 'C:\A\' because backslash in a string means to ignore the next character..
##
##abPath = os.path.join(fPath, fName)

