import glob

#to open ideas.txt and projects.txt
myfiles = glob.glob("*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read().upper())



