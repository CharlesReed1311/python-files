import FreeSimpleGUI as sg
from zip_extractor import extract_archive
sg.theme("Black")

label1 = sg.Text("Select archive:")
label2 = sg.Text("Select destination directory:")
output_label = sg.Text("",key='output',text_color="lightgreen")

input1 = sg.Input()
input2 = sg.Input()

choosebutton1 = sg.FileBrowse("Choose",key="archive")
choosebutton2 = sg.FolderBrowse("Choose",key="folder")
extractbutton = sg.Button("Extract")

col1 = sg.Column([[label1],[label2]])
col2 = sg.Column([[input1],[input2]])
col3 = sg.Column([[choosebutton1],[choosebutton2]])

window =  sg.Window("Archive Extractor",
                   layout=[[col1,col2,col3],
                           [extractbutton,output_label]])

while True:
    event, values = window.read()
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath,dest_dir)
    window['output'].update(value="Extraction complete")
    
window.close()