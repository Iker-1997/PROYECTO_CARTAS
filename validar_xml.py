import xml.etree.ElementTree as ET
def cargar(nombre):
    if nombre == "aliado":
        try:
            fitxer2 = ET.parse("myBaraja.xml")
            return fitxer2
        except ValueError:
            print("No se ha podido leer el fichero")
    if nombre == "enemi1go":
        try:
            fitxer1 = ET.parse("Enemigo.xml")
            return fitxer1
        except ValueError:
            print("No se ha podido leer el fichero")

kgmtkmgtmkgmktmg