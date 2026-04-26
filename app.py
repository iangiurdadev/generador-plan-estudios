import json

def es_prefijo_valido(input_str, palabra):
    input_str = input_str.strip().lower()

    # 1. no puede tener nada que no sean letras
    if not input_str.isalpha():
        return False

    # 2. no puede ser más largo que la palabra real
    if len(input_str) > len(palabra):
        return False

    # 3. debe coincidir como prefijo real
    return palabra.startswith(input_str)


def normalizar_condicion(x):
    x = x.strip().lower()

    if es_prefijo_valido(x, "regularizada"):
        return "regularizada"

    if es_prefijo_valido(x, "aprobada"):
        return "aprobada"

    return None

def preguntar_requisitos(tipo):
    requisitos = []

    tiene = input(f"¿Tiene requisitos para {tipo}? (si/no): ").strip().lower()
    if es_prefijo_valido(tiene,"no"):
        return requisitos

    while True:
        materia = input("ID de la materia requisito: ").strip()

        condicion = None
        while condicion is None:
            entrada = input("Condición (regularizada/aprobada): ").strip().lower()
            condicion = normalizar_condicion(entrada)

        requisitos.append({
            "para": tipo,
            "materia": materia,
            "condicion": condicion
        })

        otra = input(f"¿Agregar otro requisito para {tipo}? (si/no): ").strip().lower()
        if es_prefijo_valido(otra,"no"):
            break

    return requisitos


def crear_materia():
    id_ = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    anio = int(input("Año: "))
    cuatrimestre = int(input("Cuatrimestre: "))

    requisitos = []
    requisitos += preguntar_requisitos("cursar")
    requisitos += preguntar_requisitos("aprobar")

    materia = {
        "id": id_,
        "nombre": nombre,
        "anio": anio,
        "cuatrimestre": cuatrimestre,
        "requisitos": requisitos
    }

    return materia


def main():
    materias = []

    while True:
        materias.append(crear_materia())

        otra = input("¿Agregar otra materia? (si/no): ").strip().lower()
        if es_prefijo_valido(otra,"no"):
            break

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(materias, f, indent=2, ensure_ascii=False)

    print("Guardado en output.json")


if __name__ == "__main__":
    main()