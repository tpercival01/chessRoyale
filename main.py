import PySimpleGUI as simp

simp.theme('Dark')

layout = [
            [simp.Button('Click', size=(5, 1), key='hello'), simp.Button('Click', size=(5, 1), key='world')],
            [simp.Text('Hello', size=(5, 1)), simp.Text('World', size=(5, 1))]
         ]

window = simp.Window('Chess Royale', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == simp.WIN_CLOSED or event == 'Exit':
        break

window.close()