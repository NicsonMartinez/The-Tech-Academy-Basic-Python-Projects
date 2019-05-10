

txtFilesList = ['File1.txt', 'File10.js', 'File2.txt', 'File3.docx', 'File4.docx', 'File5.py', 'File6.html', 'File7.html', 'File8.css', 'File9.css']

fNameList = []
for i in txtFilesList:
    fullFileName = i

    charList = list(fullFileName)   # Converts string into a list of characters

    modCharList = charList[:-4]     # Erases the last four

    fName = ''.join(modCharList)    # Concatinates all of the elements into one string

    fNameList.append(fName)         
        
print("{}\n".format(txtFilesList))
print(fNameList)


    


##
##fileName = 'Hello.txt'
##
##filePath = 'C:\\A\\' #It can't be 'C:\A\' because backslash in a string means to ignore the next character..
##
##abPath = os.path.join(fPath, fName)

