import parsers
import converter

feet_inches = input("Enter feet and inches: ")

parsed = parsers.parse(feet_inches_arg=feet_inches)
converter = converter.convert_to_cm(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is {converter} cm.")


if converter < 100:
    print("Kid is too small.")
else:
    print("Kid is tall enough.")
