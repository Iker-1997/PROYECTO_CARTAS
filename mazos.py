def crearMazo(tipo, archivo):
    types = ['attack', 'defend', 'random', 'balanced']
    # Mostramos un error si el atributo <tipo> no es el deseado con la lista creada en la anterior linea.
    assert tipo in types, 'El atributo insertado no es el correcto.'

    if tipo is 'attack':
        for child in archivo.findall('deck//'):
            if child.tag == "attack" and child.text == "3":
                print(child.tag, child.text)
    elif tipo is 'defend':
        print('Defensa:', archivo)
    elif tipo is 'random':
        print('Random:', archivo)
    elif tipo is 'balanced':
        print('Balanced:', archivo)


import xml.etree.ElementTree as ET
archivoa = ET.parse('./myBaraja.xml')
archivoa = archivoa.getroot()
crearMazo('attack', archivoa)
