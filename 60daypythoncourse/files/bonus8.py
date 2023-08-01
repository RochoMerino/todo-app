
date = input("Enter the date: ")
mood = input("How did you feel: ")
thoughts = input("Let your thoughts flow: ")

with (open(f"{date}.txt", "w")) as file:
    file.write(f"Date: {date}\n")
    file.write(f"Mood: {mood}\n")
    file.write(f"Thoughts: {thoughts}\n")
