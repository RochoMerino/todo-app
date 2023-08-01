try:
    width = float(input("Width: "))
    length = float(input("Length: "))

    if length == width:
        exit("That is a square not a rectangle. Numbers can not match")

    area = width * length
    print(area)

except ValueError:
    print("Enter the digit not the word")

