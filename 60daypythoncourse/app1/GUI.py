import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do here", key="todo")
add_button = sg.Button("Add", tooltip="Add to-do to the list")
exit_button = sg.Button("Exit", tooltip="Click-here if you want to exit")

window = sg.Window('To-do application',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todolist_arg=todos)

        case sg.WIN_CLOSED:
            break

window.close()
