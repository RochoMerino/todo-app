#This code asks the user for two inputs and generates a random number between them
import random

lower_bound = int(input("Enter the lower bound:"))
upper_bound = int(input("Enter the upper bound:"))

random_number = random.randint(lower_bound,upper_bound)
print(random_number)
