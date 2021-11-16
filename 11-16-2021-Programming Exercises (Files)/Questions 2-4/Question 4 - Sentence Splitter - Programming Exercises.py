import os
os.chdir("E:\BINUS\Algorithm\get os test") #file directory

opener = open("sentenceSplitterTest.txt","r") #Opens the file
noEnter = opener.read() #Reads the file

if "Mr." in noEnter: #checks if there's "Mr." in text
    noEnter = noEnter.replace("Mr.", "Mister") #replace (["(this)"], ["(with this)"])
if "Mrs." in noEnter: #checks if there's "Mrs." in text
    noEnter = noEnter.replace("Mrs.", "Mistress") #replace (["(this)"], ["(with this)"])
if "Dr." in noEnter: #checks if there's "Dr." in text
    noEnter = noEnter.replace("Dr.", "Doctor") #replace (["(this)"], ["(with this)"])    
if "Jr." in noEnter: #checks if there's "Jr." in text
    noEnter = noEnter.replace("Jr.", "Junior") #replace (["(this)"], ["(with this)"]) 

noEnter = noEnter.replace("\n", "") #replace new line with space
noEnter = noEnter.replace(". ", ".\n") #add new line after a period
noEnter = noEnter.replace("? ", "?\n") #add new line after a question mark
noEnter = noEnter.replace("! ", "!\n") #add new line after exclamation mark

if "Mister" in noEnter: #checks if there's "Mister" in the text
    noEnter = noEnter.replace("Mister", "Mr.") #replace (["(this)"], ["(with this)"])
if "Mistress" in noEnter: #checks if there's "Mistress" in the text
    noEnter = noEnter.replace("Mistress", "Mrs.") #replace (["(this)"], ["(with this)"])
if "Doctor" in noEnter: #checks if there's "Doctor" in the text
    noEnter = noEnter.replace("Doctor", "Dr.") #replace (["(this)"], ["(with this)"])   
if "Junior" in noEnter: #checks if there's "Junior" in the text
    noEnter = noEnter.replace("Junior", "Jr.") #replace (["(this)"], ["(with this)"]) 
 
newFile = open("New and Improved Text.txt", "w") #Create a new file that can be written into
newFile.write(noEnter) #write the text we've edited into the new file

newFile.close() #close file
