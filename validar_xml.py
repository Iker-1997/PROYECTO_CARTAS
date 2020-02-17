import xml.etree.ElementTree as ET
archivo_xml = ET.parse('myBaraja.xml')
raiz = archivo_xml.getroot()
print(raiz)
for hijo in raiz:
    print(hijo.text)