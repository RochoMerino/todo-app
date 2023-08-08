import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input("")
button1 = sg.FilesBrowse("Choose", tooltip="Choose file", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input("")
button2 = sg.FolderBrowse("Choose", tooltip="Choose folder", key="folder")


compress_button = sg.Button("Compress", tooltip="Compress files")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_button], [output_label]])

while True:
    event, values = window.read()
    print(event, values)

    filepaths = values["files"].split(";")
    folder = values["folder"]

    make_archive(filepaths, folder)

    window["output"].update(value="Compression Completed")

window.close()
