import xml.etree.ElementTree as ET
def cargar(nomobre):
    if nombre == "aliado":
        try:
            fitxer2 = ET.parse("myBaraja.xml")
            return fitxer2
        except ValueError:
            print("No se ha podido cargar el fichero")
    else:
        try:
            fitxer1 = ET.parse("Enemigo.xml")
            return fixter1
        except ValueError:
            print("no se ha podido cargar el fichero")