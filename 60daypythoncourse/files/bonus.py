contents= ["Carrots in the kitchen", 
           "Submarine in titanic", 
           "Renting a girlfriend"]


filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(filename, "w")
    file.write(content)

