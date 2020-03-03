import random
import xml.etree.ElementTree as ET
archivo = ET.parse('./myBaraja.xml')
archivo = archivo.getroot()
def crearMazo(archivo):
    llista_general = [] ##llista dels diccionaris
    card = {} ##emmagatzema la info de les cartes
    i=0
    while i<10: ##farem el pas 10 vegades per agafar les 10 cartes
        x = str(random.randint(1,20))
        for child in archivo.findall('.//card['+x+']'): ##Agafara cadascun dels fills de //card
            for child2 in child:
                card['summonPoints']=child.attrib['summonPoints'] ##Per afegir els atributs al diccionari
                card['type']=child.attrib['type']
                card[child2.tag] = child2.text ##Per agafar i posar al diccionari l'etiqeta i el contingut
            if card in llista_general: ##Si la carta es troba a la llista, no lagafara i afegira una altre q no es trobi
                pass
            else:
                i=i+1
                llista_general.append(card)
            card = {}
    print(len(llista_general))
    return llista_general
print(crearMazo(archivo))
