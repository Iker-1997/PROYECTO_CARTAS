import xml.etree.ElementTree as ET


def cargar(nombre):
    if nombre == "aliado":
        try:
            fitxer2 = ET.parse("myBaraja.xml")
            return fitxer2
        except ValueError:
            print("No se ha podido leer el fichero")
    # La otra opcion...
    else:
        try:
            fitxer1 = ET.parse("Enemigo.xml")
            return fitxer1
        except ValueError:
            print("No se ha podido leer el fichero")