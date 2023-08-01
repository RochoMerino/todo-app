import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do here") #tooltip funciona para cuando estes hovering above algo te dice que hacer
add_button = sg.Button("Add",tooltip="Add to-do to the list")


window = sg.Window('To-do application', layout=[[label], [input_box, add_button]])
window.read()
window.close()
