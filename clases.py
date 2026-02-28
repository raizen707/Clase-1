#tipo de dato , nombreVariable = valor
Edad: int = 25
Nombre: str = "Francisco"
Estatura: float = 1.75
EsEstudiante: bool = True
EstadoCivil: str = "Soltero"
Habilidades: list = ["Programación", "Diseño Gráfico", "Gestión de Proyectos"]
ListaVariables: list = [Edad, Nombre, Estatura, EsEstudiante, EstadoCivil, Habilidades]

print(Habilidades[0])

#Imprimir en consola
print("Edad:", Edad)
print("Nombre:", Nombre)
print("Estatura:", Estatura)
print("Es Estudiante:", EsEstudiante)
print("Estado Civil:", EstadoCivil)
print("Habilidades:", Habilidades)  
#Algororitmo -> secuencia de pasos para resolver un problema

#Ejemplo de Juego COD
#Metodos o funciones , algoritmos
def validar_hardware(cpu: str, ram: int, gpu: str, almacenamiento: int, 
                     es_gaming: bool, os: str, npu: bool, es_paraIA: bool, modelos_ia: list) -> None:
    print("Validando hardware...")
    if cpu in ["Intel i7-14700K", "AMD Ryzen 9 7900X"]:
        print("El CPU es adecuado.")
    if es_gaming:
        if ram >= 16 and gpu in ["NVIDIA RTX 3060", "AMD RX 6600"]:
            if almacenamiento >= 512:
                print("El hardware es adecuado para juegos.")
            else:
                print("El almacenamiento es insuficiente para juegos.")
            print("El hardware es adecuado para juegos.")
        else:
            print("El hardware no es adecuado para juegos.")
    elif es_paraIA:
        if npu and ram >= 32:
            print("El hardware es adecuado para IA.")
            if almacenamiento >= 1024:
                print("El almacenamiento es suficiente para IA.")
                if os in ["Windows 11", "Linux Ubuntu"]:
                    print("El sistema operativo es compatible con IA.")
                if gpu in ["NVIDIA RTX 3060", "AMD RX 6600"]:
                    print("La GPU es adecuada para IA.")
        else:
            print("El hardware no es adecuado para IA.")
    else:
        if ram >= 8:
            print("El hardware es adecuado para uso general.")
        else:
            print("El hardware no es adecuado para uso general.")

# validar_hardware(
#     cpu="Intel i7-14700K",
#     ram=32,
#     gpu="NVIDIA RTX 3060",
#     almacenamiento=2048,
#     es_gaming=True,
#     os="Windows 11",
#     npu=True,
#     es_paraIA=False
# )


#clase 3
def Menu() -> None:
    print("----- Menú Principal -----")
    print("Ingrese tipo de cpu:")   
    menu_cpu()
    opcion_cpu = input("Seleccione una opción (1-3): ")
    cpu_nombre = retornar_cpu(opcion_cpu)
    print("CPU seleccionada:", cpu_nombre)
    ram = int(input("Ingrese la cantidad de RAM (en GB): "))
    menu_gpu()
    opcion_gpu = input("Seleccione una opción (1-3): ")
    gpu_nombre = retornar_gpu(opcion_gpu)
    print("GPU seleccionada:", gpu_nombre)

    almacenamiento = int(input("Ingrese la capacidad de almacenamiento (en GB): "))
    es_gaming_input = input("¿Es para gaming? (s/n): ")
    es_gaming = es_gaming_input.lower() == 's'
    es_paraIA_input = input("¿Es para IA? (s/n): ")
    es_paraIA = es_paraIA_input.lower() == 's'
    menu_os()
    opcion_os = input("Seleccione una opción (1-3): ")
    os_nombre = retornar_os(opcion_os)
    print("Sistema Operativo seleccionado:", os_nombre)
    if es_paraIA:
        cantidad_modelos_ia = int(input("¿Cuántos modelos de IA desea usar? "))
        modelos_ia = []
        for i in range(cantidad_modelos_ia):
            menu_modelos_ia()
            opcion_modelos_ia = input(f"Seleccione el modelo de IA #{i+1} (1-7): ")
            modelo_ia_nombre = retornar_modelos_ia(opcion_modelos_ia)
            print(f"Modelo de IA #{i+1} seleccionado:", modelo_ia_nombre)
            modelos_ia.append(modelo_ia_nombre)

    validar_hardware(
        cpu=cpu_nombre,
        ram=ram,
        gpu=gpu_nombre,
        almacenamiento=almacenamiento,
        es_gaming=es_gaming,
        os=os_nombre,
        npu=True,
        es_paraIA=es_paraIA,
        modelos_ia=modelos_ia
    )
def menu_os() -> None:
    print("1. Windows 11")
    print("2. macOS Ventura")
    print("3. Linux Ubuntu")

def retornar_os(opcion_os: str) -> str:
    os_dict = {
        "1": "Windows 11",
        "2": "macOS Ventura",
        "3": "Linux Ubuntu"
    }
    return os_dict.get(opcion_os, "Opción inválida")

def menu_cpu() -> None:
    print("1. Intel")
    print("2. AMD")
    print("3. ARM")
def retornar_cpu(opcion_cpu: str) -> str:
    cpu_dict = {
        "1": "Intel",
        "2": "AMD",
        "3": "ARM"
    }
    return cpu_dict.get(opcion_cpu, "Opción inválida")
def menu_gpu() -> None:
    print("1. NVIDIA RTX 3060")
    print("2. AMD RX 6600")
    print("3. Intel Iris Xe")

def retornar_gpu(opcion_gpu: str) -> str:
    gpu_dict = {
        "1": "NVIDIA RTX 3060",
        "2": "AMD RX 6600",
        "3": "Intel Iris Xe"
    }
    return gpu_dict.get(opcion_gpu, "Opción inválida")

def menu_modelos_ia() -> None:
    print("1. GPT-5")
    print("2. Claude")
    print("3. Llama 4")
    print("4. Gemini 1.5")
    print("5. Mistral 7B")
    print("6. Falcon 180B")
    print("7. Cerebras-GPT 111B")

def retornar_modelos_ia(opcion_modelos_ia: str) -> str:
    modelos_ia_dict = {
        "1": "GPT-5",
        "2": "Claude",
        "3": "Llama 4",
        "4": "Gemini 1.5",
        "5": "Mistral 7B",
        "6": "Falcon 180B",
        "7": "Cerebras-GPT 111B"
    }
    return modelos_ia_dict.get(opcion_modelos_ia, "Opción inválida")

Menu()