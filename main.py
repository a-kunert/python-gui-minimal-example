import PySimpleGUI as Gui

input_column = [
    [
        Gui.In(size=(30, 1), enable_events=True, key="input_field"),
        Gui.Button('Run', enable_events=True, key="confirm_button")
    ]
]

result_column = [
    [Gui.Text(size=(30, 1), key="output_field")]
]

layout = [
    [
        Gui.Column(input_column),
        Gui.VSeparator(),
        Gui.Column(result_column)
    ]
]

window = Gui.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == Gui.WIN_CLOSED:
        break
    if event == 'input_field':
        pass
    if event == 'confirm_button':
        val = values["input_field"]
        if val == "":
            output = ""
        else:
            val = int(val)
            output = 2 * val
        window["output_field"].update(output)

window.close()