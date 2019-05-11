##DRILL:
##Drill Description:
##For this drill, you will need to write a script that creates a database and adds new data
##into that database.
##
##Requirements:
##Your script will need to use Python 3 and the sqlite3 module.
##
##Your database will require 2 fields, an auto-increment primary integer field and a field
##with the data type of string.
##
##Your script will need to read from the supplied list of file names at the bottom of this
##page and determine only the files from the list which ends with a “.txt” file extension.
##
##Next, your script should add those file names from the list ending with “.txt” file
##extension within your database.
##
##Finally, your script should legibly print the qualifying text files to the console
##
##By: Nicson Martinez
##Date: 5/10/2019


import sqlite3

##Additional Setup Instructions:
##The following is the list of file names to use for this drill:

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#----------------------------------------------------------------

conn = sqlite3.connect('myDatabase.db')

print("Our 'fileList' tuple has:\n\n{}\n\n".format(fileList))

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_myTxtFiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_textFile TEXT\
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('myDatabase.db')

with conn:
    cur = conn.cursor()
    count = 0
    print("The qualifying text files from the 'fileList' tuple are:\n")
    for file in fileList:
        if file.endswith('.txt'):
            count += 1
            print("{}) {}".format(count,file))
            cur.execute("INSERT INTO tbl_myTxtFiles(col_textFile) VALUES (?)", (file,))
    conn.commit()
conn.close()

