import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input("")
button1 = sg.FilesBrowse("Choose", tooltip="Choose file")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input("")
button2 = sg.FolderBrowse("Choose", tooltip="Choose folder")

compress_button = sg.Button("Compress", tooltip="Compress files")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_button]])

window.read()
window.close()
