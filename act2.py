import json
import os

DIRECTORIO_CLIENTES = "archivos_clientes"
if not os.path.exists(DIRECTORIO_CLIENTES):
    os.makedirs(DIRECTORIO_CLIENTES)

clientes_hash = {}

usuarios = {
    "usuario1": "Paulina - Ejecutivo",
    "usuario2": "Andrea - Supervisor"
}

def crear_cliente(nombre, servicio):
    """Crea un nuevo archivo JSON para un cliente nuevo."""
    if nombre in clientes_hash:
        print(f"El cliente '{nombre}' ya existe.")
        return
    datos = {"nombre": nombre, "servicios": [servicio]}
    archivo = os.path.join(DIRECTORIO_CLIENTES, f"{nombre}.json")
    with open(archivo, 'w') as f:
        json.dump(datos, f)
    clientes_hash[nombre] = archivo
    print(f"Cliente '{nombre}' creado con el servicio '{servicio}'.")

def actualizar_cliente(nombre, servicio):
    """Agrega un nuevo servicio a un cliente existente."""
    archivo = clientes_hash.get(nombre)
    if not archivo or not os.path.exists(archivo):
        print(f"Cliente '{nombre}' no encontrado.")
        return
    with open(archivo, 'r') as f:
        datos = json.load(f)
    datos["servicios"].append(servicio)
    with open(archivo, 'w') as f:
        json.dump(datos, f)
    print(f"Servicio '{servicio}' agregado al cliente '{nombre}'.")

def leer_cliente(nombre):
    """Muestra la información de un cliente."""
    archivo = clientes_hash.get(nombre)
    if not archivo or not os.path.exists(archivo):
        print(f"Cliente '{nombre}' no encontrado.")
        return
    with open(archivo, 'r') as f:
        datos = json.load(f)
    print(f"Cliente: {datos['nombre']}, Servicios: {datos['servicios']}")

def eliminar_cliente(nombre):
    """Elimina el archivo de un cliente y lo remueve del diccionario."""
    archivo = clientes_hash.get(nombre)
    if not archivo or not os.path.exists(archivo):
        print(f"Cliente '{nombre}' no encontrado.")
        return
    os.remove(archivo)
    del clientes_hash[nombre]
    print(f"Cliente '{nombre}' eliminado.")

def listar_clientes():
    """Muestra una lista de todos los clientes registrados."""
    if not clientes_hash:
        print("No hay clientes registrados.")
    else:
        print("Clientes registrados:", list(clientes_hash.keys()))

def simulacion(usuario, accion, nombre=None, servicio=None):
    print(f"\nAcción por {usuarios[usuario]}")
    if accion == "crear" and nombre and servicio:
        crear_cliente(nombre, servicio)
    elif accion == "actualizar" and nombre and servicio:
        actualizar_cliente(nombre, servicio)
    elif accion == "leer" and nombre:
        leer_cliente(nombre)
    elif accion == "eliminar" and nombre:
        eliminar_cliente(nombre)
    elif accion == "listar":
        listar_clientes()
    else:
        print("Acción no reconocida o parámetros incompletos.")

if __name__ == "__main__":
    simulacion("usuario1", "crear", "Santiago", "Telefonía")
    simulacion("usuario2", "crear", "José", "Tv")
    simulacion("usuario1", "actualizar", "Santiago", "TV de paga")
    simulacion("usuario2", "leer", "Santiago")
    simulacion("usuario1", "listar")
    simulacion("usuario2", "eliminar", "Jose")
    simulacion("usuario1", "listar")
