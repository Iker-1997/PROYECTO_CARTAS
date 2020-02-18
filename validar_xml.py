import xml.etree.ElementTree as ET
def cargar(nomobre):
    if nombre == "aliat":
        try:
            fitxer2 = ET.parse("myBaraja.xml")
            return fitxer2
        except ValueError:
            print("No sha pogut carregar el fitxer")
    else:
        try:
            fitxer1 = ET.parse("Enemigo.xml")
            return fixter1
        except ValueError:
            print("No sha pogut carregar el fitxer")