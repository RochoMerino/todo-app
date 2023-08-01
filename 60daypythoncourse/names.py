nombres = ["Rodrigo", "Maria", "Julieta"]
nombres.sort(reverse=True)

for index, names in enumerate(nombres, start=1):
    row = f"{index}. {names.title()}"
    print(row)