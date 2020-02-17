from xml.dom import minidom
archivo = minidom.parse('mybaraja.xml')
rai
for playerconfig in
playerlife= archivo.getElementsByTagName("playerLife")[0]
print(playerlife.firstChild.data)
summonpoints = archivo.getElementsByTagName("summonPointsPlayer")[0]
print(summonpoints.sChild.data)