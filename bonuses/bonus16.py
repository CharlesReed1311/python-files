import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choosebutton1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choosebutton2 = sg.FolderBrowse("Choose", key="folder")

compressbutton = sg.Button("Compress")
output_label = sg.Text("",key='output')

window =  sg.Window("File Compressor", 
                    layout=[[label1,input1,choosebutton1], 
                            [label2,input2,choosebutton2], 
                            [compressbutton,output_label]])

while True:
        event, values = window.read()
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window['output'].update(value="Compression complete")
        
window.close()