def get_average():
    with open(r"C:\Users\Rocho\OneDrive\Escritorio\P\60daypythoncourse\files\data\datafiles.txt", "r") as file:
        data = file.readlines()
    
    values = data[1:]


    values = [float(value.strip("\n")) for value in values]
    average_local = sum(values) / len(values)

    return average_local



average = get_average()
print(average)
