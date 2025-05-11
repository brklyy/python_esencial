print_opciones = [
    "Agregar una tarea",
    "Mostrar todas las tareas",
    "Marcar una tarea como completada",
    "Eliminar una tarea",
    "Salir del programa"
]    


def agregar_tarea(lista):
    descripcion = input("Introduce la descripción de la tarea: ")

    tarea = {
        "desc": descripcion,
        "estado": "Pendiente"
    }
    lista.append(tarea)

    print("Tarea agregada exitosamente")


def mostrar_tarea(lista):
    if not lista:
        print("La agenda está vacía.")
    else:
        for i, tarea in enumerate(lista, 1):
            print(f"{i}. {tarea['desc'] - {tarea['estado']}}")


def mostrar_menu():
    for i, opciones in enumerate(print_opciones, 1):
        print(f"{i}. {opciones}")


def marcar_completo(lista):
    if not lista:
        print("No hay tareas para completar")
        return
    
    print("Tareas en proceso:")
    for i, tarea in enumerate(lista, 1):
        print(f"{i}. {tarea['desc']} - {tarea['estado']}")

    try:
        indice = int(input("Código de la tarea que quieres marcar: "))
        if 1 <= indice <= len(lista):
            if lista[indice - 1]["estado"] == "Completado":
                print("Tarea ya completada.")
            else:
                lista[indice - 1]["estado"] = "Completado"
                print("Tarea ya marcada como completada.")
        else:
            print("Número de índice fuera de rango.")
    except ValueError:
        print("Entrada no válida.")


def eliminar_tarea(lista):
    if not lista:
        print("No hay tareas para eliminar")
        return

    print("Tareas en proceso:")
    for i, tarea in enumerate(lista, 1):
        print(f"{i}. {tarea['desc']} - {tarea['estado']}")
    
    try:
        indice = int(input("Introduce el código de la tarea que deseas eliminar: "))
        if 1 <= indice <= len(lista):
            tarea_eliminada = lista.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada['desc']}' eliminada correctamente")
        else:
            print("Número fuera de rango")
    except:
        print("Entrada no válida")





tarea = []
agregar_tarea(tarea)
mostrar_tarea(tarea)


    

    
    
    



