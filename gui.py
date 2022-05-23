import PySimpleGUI as sg
from Scrap.main import Functions


exe = Functions()


sg.change_look_and_feel('DarkAmber')

#--------------------------------------LOGIN--------------------------------------------------------------------------
layout=[
    [sg.Text('Automate ', size=(100, 1), justification='center', font=("Helvetica", 20), relief=sg.RELIEF_RIDGE)],
    [sg.Text('', size=(15, 1), font=("Helvetica", 15))],
    [sg.Text('Selecione o Excel:', size=(20,0), font=("Helvetica", 12))],
    [[sg.In(size=(31, 6), key='file', font=("Helvetica", 12)) ,sg.FileBrowse(file_types=(("Excel CODIGOS", "*.xlsx"),))]],
    [sg.Text('Selecione a Data:', size=(15,0), font=("Helvetica", 12))],
    [sg.CalendarButton('Calendario', format='%m/%Y', key=("date"))],
    [sg.Radio('Scrap', "RADIO1", default=True, key=("task")), sg.Radio('Cupons', "RADIO1", key=("task"))],
    [sg.Text('', size=(7,0))], 
    [sg.Text('Finalizado!', size=(30,1), font=("Helvetica", 15),  visible=False, key='-CBOX-')], 
    [sg.Text('', size=(16,0)), sg.Button('INICIAR', border_width=5, size=(20, 1), key="run")],
    [sg.Text('', size=(2,0)), sg.Output(size=(50,5))]
    ]

window = sg.Window('Automate', layout, size=(450, 450))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancelar'):
        break

    elif event == 'run':
        if exe.readExcel(values['file']):
            #exe.start(values['date'])
            exe.teste()

        window['-CBOX-'].Update(visible=True)

window.close()