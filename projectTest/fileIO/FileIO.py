# Reading
file = open("example.txt", "r")


line = file.readline()
print(f"line: {line}, length: {len(line)}", end="\n\n")


# Line one is already read thus will get only next line
data = file.read()
print(data)
print(type(data))


file.close()

"""
Hello Ujjwal Pandey!!
I am a programmer!
I love programming.
"""

# When open in write mode it takes all the data form file and clears the file txt, like created new file.

# Create new file
newFile = open("newfile.txt", "w")
newFile.close()


# Create new file with new data
newFile = open("newfile2.txt", "w")
newFile.write("Sample data...")
newFile.close()


# Writing
fileTxt = open("example.txt", "w")
fileTxt.write("This is new data")
fileTxt.close()

# Append text
fileTxt = open("example.txt", "a")
fileTxt.write("""
This is new appended data
Hello Ujjwal Pandey!!
I am a programmer!
I love programming.""")     # Write at end
fileTxt.write("\nABC")      # Write at end
fileTxt.close()



# Replace data
fileA = open("example.txt", "r")
r = fileA.read()
print(r)
newTxt = r.replace("Pandey", "Pandey ji")
fileA.close()

fileB = open("example.txt", "w")
fileB.write("This is new txt\n\n" + newTxt)
fileB.close()

def replaceDataInSimpleWay():
    # Replace data in simple way
    with  open("example.txt", "r") as fileA:
        r = fileA.read()
        print(r)
        newTxt = r.replace("Pandey", "Pandey ji")

    with open("example.txt", "w") as fileB:
        fileB.write("This is new txt\n\n" + newTxt)

# replaceDataInSimpleWay()