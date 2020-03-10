import random
import xml.etree.ElementTree as ET


def aleatorio(archivoa):
    archivo = archivoa.getroot()
    llista_general = []  # llista dels diccionaris
    card = {}  # emmagatzema la info de les cartes
    i = 0
    while i < 10:  # farem el pas 10 vegades per agafar les 10 cartes
        x = str(random.randint(1, 20))
        for child in archivo.findall('.//card['+x+']'):  # Agafara cadascun dels fills de //card
            for child2 in child:
                card['summonPoints'] = child.attrib['summonPoints']  # Per afegir els atributs al diccionari
                card['type'] = child.attrib['type']
                card[child2.tag] = child2.text  # Per agafar i posar al diccionari l'etiqeta i el contingut
            if card in llista_general:  # Si la carta es troba a la llista, no lagafara i afegira una altre que no es trobi
                pass
            else:
                i = i+1
                llista_general.append(card)
            card = {}
    print(len(llista_general))
    return llista_general


def ataque(archivoa):
    archivo = archivoa.getroot()
    llista_general = []  # llista dels diccionaris
    card = {}  # emmagatzema la info de les cartes
    d = 5
    while True:  # farem el pas 10 vegades per agafar les 10 cartes
        for child in archivo.findall('.//card[attack="'+str(d)+'"]'):  # Agafara cadascun dels fills de //card
            for child2 in child:
                card['summonPoints'] = child.attrib['summonPoints']  # Per afegir els atributs al diccionari
                card['type'] = child.attrib['type']
                card[child2.tag] = child2.text  # Per agafar i posar al diccionari l'etiqeta i el contingut
            if child in llista_general:
                pass
            else:
                llista_general.append(card)
            card = {}
            if len(llista_general) == 10:  # Quan la llista arriba a 10, ens la retorna
                print(len(llista_general))
                return llista_general
        d = d - 1


def defensa(archivoa):
    archivo = archivoa.getroot()
    llista_general = []  # llista dels diccionaris
    card = {}  # emmagatzema la info de les cartes
    d = 5
    while True:  #farem el pas 10 vegades per agafar les 10 cartes
        for child in archivo.findall('.//card[defense="'+str(d)+'"]'):  # Agafara cadascun dels fills de //card
            for child2 in child:
                card['summonPoints'] = child.attrib['summonPoints']  # Per afegir els atributs al diccionari
                card['type'] = child.attrib['type']
                card[child2.tag] = child2.text  # Per agafar i posar al diccionari l'etiqeta i el contingut
            if child in llista_general:
                pass
            else:
                llista_general.append(card)
            card = {}
            if len(llista_general) == 10:  # Quan la llista arriba a 10, ens la retorna
                print(len(llista_general))
                return llista_general
        d = d - 1


def equilibrado(archivoa):
    archivo = archivoa.getroot()
    llista_general = []  # llista dels diccionaris
    card = {}  # emmagatzema la info de les cartes
    d = 0
    while True:  # farem el pas 10 vegades per agafar les 10 cartes
        for child in archivo.findall('.//card'):  # Agafara cadascun dels fills de //card
            for child2 in child:
                card['summonPoints'] = child.attrib['summonPoints']   # Per afegir els atributs al diccionari
                card['type'] = child.attrib['type']
                card[child2.tag] = child2.text  # Per agafar i posar al diccionari l'etiqeta i el contingut
            at = int(child.find("attack").text)  # Agafem els valors d'atac
            df = int(child.find("defense").text)  # Agafem els valors de defensa
            if at > df:  # Per tal de no fer el valor absolut, agafem quin es el valor mes gran i li restem el mes petit
                dif = at - df
            else:
                dif = df - at
            if child in llista_general:
                pass
            else:
                if dif == d:  # Mirem si les diferencies es igual a 0, sino anem augmentant
                    llista_general.append(card)
            card = {}
            if len(llista_general) == 10:  # Quan la llista arriba a 10, ens la retorna
                print(len(llista_general))
                return llista_general
        d = d + 1


