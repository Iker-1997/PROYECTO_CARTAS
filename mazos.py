import random
def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'

    for i in range(10):
        x = str(random.randint(1,10))
        llista_general = []
        for child in archivo.findall('.//card['+x+']'):
            for child2 in child:
                print(child2.tag, child2.text, child2.attrib)
                llista_general.append(child)


import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
crearMazo('attack', archivoa)
import random

