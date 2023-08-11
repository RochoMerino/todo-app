
while True:
    accion = input("add, show, edit, complete or exit: ")
    accion = accion.lower()
    accion = accion.strip()

    match accion:
        case "add":
            todo = input("Enter a to-do list item: ") + "\n"

            #file = open(r"C:\Users\rocho\OneDrive\Escritorio\P\todo.txt", "r") # si es que todo.txt esta en otro folder tienes que poner la ruta completa ejemplo files/todo.txt
            #todolist = file.readlines()
            #file.close()
            with (open(r"/60daypythoncourse/app1/todo.txt", "r")) as file:
                todolist = file.readlines()

            todolist.append(todo)

            #file = open(r"C:\Users\rocho\OneDrive\Escritorio\P\todo.txt", "w") # w = write r = read a = append
            #file.writelines(todolist)
            #file.close()
            with (open(r"/60daypythoncourse/app1/todo.txt", "w")) as file:
                file.writelines(todolist)


        case "show":

            #file = open(r"C:\Users\rocho\OneDrive\Escritorio\P\todo.txt", "r")
            #todolist = file.readlines()
            #file.close()
            with (open(r"/60daypythoncourse/app1/todo.txt", "r")) as file:
                todolist = file.readlines()

            #new_todos = []
            #for item in todolist:
            #    new_item = item.strip("\n")
            #    new_todos.append(new_item)

            #new_todos = [item.strip("\n") for item in todolist]
            #tambien puedes usar list comprehension si tienes tipo numbers = [1, 2 ,3.1] para juntarlos asi numbers = sum([float(number) for number in numbers]) y de los convierte en float y despues los suma

            for index, item in enumerate(todolist, start=1):
                item = item.strip("\n")
                row = (f"{index}. {item}")
                print(row)

        case "exit":
            break

        case "edit":
            number = int(input("Enter the number of the to-do you want to edit: "))
            number = number - 1

            with (open(r"/60daypythoncourse/app1/todo.txt", "r")) as file:
                todolist = file.readlines()

            new_todo = input("Enter the new to-do: ")
            todolist[number] = new_todo + "\n"

            with (open(r"/60daypythoncourse/app1/todo.txt", "w")) as file:
                file.writelines(todolist)

        case"complete":
            number = int(input("Enter the number of the to-do you have completed: "))

            with (open(r"/60daypythoncourse/app1/todo.txt", "r")) as file:
                todolist = file.readlines()

            todo_to_remove = todolist[number - 1].strip("\n")
            todolist.pop(number - 1)

            with (open(r"/60daypythoncourse/app1/todo.txt", "w")) as file:
                file.writelines(todolist)

            message = f"You have removed {todo_to_remove} from the to-do list"
            print(message)

        case unkown_case:
            print("That is not an option")

