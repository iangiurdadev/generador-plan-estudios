import json

def preguntar_requisitos(tipo):
    requisitos = []

    tiene = input(f"¿Tiene requisitos para {tipo}? (si/no): ").strip().lower()
    if tiene != "si":
        return requisitos

    while True:
        materia = input("ID de la materia requisito: ").strip()
        condicion = input("Condición (regularizada/aprobada): ").strip().lower()

        requisitos.append({
            "para": tipo,
            "materia": materia,
            "condicion": condicion
        })

        otra = input("¿Agregar otro requisito? (si/no): ").strip().lower()
        if otra != "si":
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
        if otra != "si":
            break

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(materias, f, indent=2, ensure_ascii=False)

    print("Guardado en output.json")


if __name__ == "__main__":
    main()