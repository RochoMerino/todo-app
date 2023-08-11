import PySimpleGUI as sg
from converter import convert_to_cm

text1 = sg.Text("Enter feet: ")
input1 = sg.Input("", key="feet")

text2 = sg.Text("Enter inches: ")
input2 = sg.Input("", key="inches")

button = sg.Button("Convert")

output_label = sg.Text(key="answer", text_color="Red")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[text1, input1],
                                        [text2, input2],
                                        [button, output_label, exit_button]])

while True:
    event, value = window.read()
    print(event, value)

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    feet = float(value["feet"])
    inches = float(value["inches"])

    answer = convert_to_cm(feet, inches)

    window["answer"].update(value=f"{answer} cm")


window.close()
