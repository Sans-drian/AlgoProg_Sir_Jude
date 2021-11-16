import os
os.chdir("E:\BINUS\Algorithm\get os test") #file directory

fileOpen = open("exerpt.txt","r") #Opens and reads the file
fileRead = fileOpen.read() 

lowDelWord = fileRead.lower().replace(".", "") #change word into lowercase and remove punctuations.

fileSplit = len(lowDelWord.split()) #count the amount of words
fileTextLen = len(lowDelWord) #count the length of words

aveWordLen = fileTextLen / fileSplit #calculate the average

fileOpen.close()

print(f"The average word length is {aveWordLen}")
print(f"The sum of all the lengths of word tokens is {fileTextLen}") #print with text
print(f"The amount of words in the text is {fileSplit}")

# print(aveWordLen)
# print(fileTextLen)
# print(fileSplit)
