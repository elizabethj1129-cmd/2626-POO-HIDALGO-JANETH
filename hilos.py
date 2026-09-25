import threading

# Ejemplo sencillo de uso de hilos con un Lock (mutex) para proteger
# un contador global compartido.

contador_global = 0
mutex = threading.Lock()

def incrementar():
    """Incrementa el contador global de forma segura usando el mutex."""
    global contador_global
    with mutex:
        contador_global += 1

def tarea(veces: int):
    for _ in range(veces):
        incrementar()

def main():
    repeticiones = 100_000

    hilo1 = threading.Thread(target=tarea, args=(repeticiones,))
    hilo2 = threading.Thread(target=tarea, args=(repeticiones,))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print("El valor final del contador global es:", contador_global)

if __name__ == "__main__":
    main()

