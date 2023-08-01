filename = ["1.Perritos.txt", "2.Carros.txt", "3.Gatos.txt"]

for i in filename:
    i = i.replace(".", " - ", 1)
    print(i)


