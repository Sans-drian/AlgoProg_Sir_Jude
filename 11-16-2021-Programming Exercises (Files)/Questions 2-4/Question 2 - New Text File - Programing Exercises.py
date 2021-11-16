import os
os.chdir("E:\BINUS\Algorithm\get os test") #file directory

fileOpen = open("exerpt.txt","r") #Opens and reads the file
reader = fileOpen.readlines() #Reads each lines of fileOpen

newFile = open("Your New File.txt", "w") #Creates new files and writes in it

numLine = 1 #counter for the number of lines

for lines in reader:
    newFile.write("Line {}: {}".format(numLine, lines)) #write in newFile and add Line {numLine}      
    numLine += 1 #add 1 to counter

print("Your new file has been created, please check your designated folder location.") #tell user what has happened

fileOpen.close #close files
newFile.close
