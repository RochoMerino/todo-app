import PySimpleGUI as sg
from extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select Archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archieve")

label2 = sg.Text("Select destination")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="Output", text_color="green")

window = sg.Window("Archive extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    destination_directory = values["folder"]
    extract_archive(archivepath, destination_directory)
    window["output"].update(value="Extraction Completed")
window.close()