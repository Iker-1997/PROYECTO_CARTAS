import random
import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
def crearMazo(archivo):
    llista_general = []
    card = {}
    i=0
    while i<10:
        x = str(random.randint(1,10))
        for child in archivo.findall('.//card['+x+']'):
            for child2 in child:
                card[child2.tag] = child2.text
            if card in llista_general:
                pass
            else:
                i=i+1
                llista_general.append(card)
            card = {}
    print(len(llista_general))
    return llista_general
print(crearMazo(archivoa))
