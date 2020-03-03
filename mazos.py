import random
def crearMazo(archivo):
    deck = []
    card = {}
    for i in range(10):
        x = str(random.randint(1,10))
        for child in archivo.findall('.//card['+x+']'):
            for child2 in child:
                card[child2.tag] = child2.text
        deck.append(card)
        print(deck)



import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
crearMazo(archivoa)


r