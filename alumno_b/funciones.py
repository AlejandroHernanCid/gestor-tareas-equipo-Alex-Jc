from colorama import Fore, Style
from pathlib import Path
fich = Path("tareas.txt")
 

def marcar_completada(fichero):
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No hay tareas para marcar." + Style.RESET_ALL)
            return

        print(Fore.CYAN + "--- Tareas Actuales ---" + Style.RESET_ALL)
        for i, tarea in enumerate(tareas):
            tarea_clean = tarea.strip()
            # Manejar tareas con o sin prefijo [COMPLETADA]
            if tarea_clean.startswith("[COMPLETADA]"):
                descripcion = tarea_clean.replace("[COMPLETADA]", "").strip()
                print(f"{i + 1}. " + Fore.GREEN + "[✓] {descripcion}" + Style.RESET_ALL)
            else:
                print(f"{i + 1}. " + Fore.YELLOW + "[ ] {tarea_clean}" + Style.RESET_ALL)
        
        print(Style.RESET_ALL)

        while True:
            try:
                num_tarea = int(input("Introduce el número de la tarea a marcar como completada: "))
                if 1 <= num_tarea <= len(tareas):
                    break
                else:
                    print(Fore.RED + "Número de tarea fuera de rango." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)

        idx_tarea = num_tarea - 1
        tarea_actual = tareas[idx_tarea].strip()

        if tarea_actual.startswith("[COMPLETADA]"):
            print(Fore.YELLOW + "Esta tarea ya estaba completada." + Style.RESET_ALL)
        else:
            tareas[idx_tarea] = f"[COMPLETADA] {tarea_actual}\n"
            with open(fichero, "w", encoding="utf-8") as f:
                f.writelines(tareas)
            print(Fore.GREEN + "¡Tarea marcada como completada!" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"El fichero {fichero} no existe." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Ha ocurrido un error: {e}" + Style.RESET_ALL)

def eliminar_tarea(fichero):
    """Elimina una tarea del fichero."""
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            tareas = f.readlines()

        if not tareas:
            print(Fore.YELLOW + "No hay tareas para eliminar." + Style.RESET_ALL)
            return

        print(Fore.CYAN + "--- Tareas Actuales ---" + Style.RESET_ALL)
        for i, tarea in enumerate(tareas):
            tarea_clean = tarea.strip()
            # Manejar tareas con o sin prefijo [COMPLETADA]
            if tarea_clean.startswith("[COMPLETADA]"):
                descripcion = tarea_clean.replace("[COMPLETADA]", "").strip()
                print(f"{i + 1}. " + Fore.GREEN + "[✓] {descripcion}" + Style.RESET_ALL)
            else:
                print(f"{i + 1}. " + Fore.YELLOW + "[ ] {tarea_clean}" + Style.RESET_ALL)
        
        print(Style.RESET_ALL)

        while True:
            try:
                num_tarea = int(input("Introduce el número de la tarea a eliminar: "))
                if 1 <= num_tarea <= len(tareas):
                    break
                else:
                    print(Fore.RED + "Número de tarea fuera de rango." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)

        tareas.pop(num_tarea - 1)

        with open(fichero, "w", encoding="utf-8") as f:
            f.writelines(tareas)
        
        print(Fore.GREEN + "¡Tarea eliminada correctamente!" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"El fichero {fichero} no existe." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Ha ocurrido un error: {e}" + Style.RESET_ALL)

def despedida():
    """Muestra mensaje de despedida."""
    print(Fore.MAGENTA + "¡Hasta luego! Gracias por usar el gestor de tareas." + Style.RESET_ALL)
