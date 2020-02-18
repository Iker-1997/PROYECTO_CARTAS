import xml.etree.ElementTree as ET
tree = ET.parse('myBaraja.xml')
root = tree.getroot()
print(root)
print(tree)
for child in root:
    print(child.tag,child.attrib)
    for child2 in child:
        print(child2.tag,child2.attrib)
        for child3 in child2:
            print(child3.tag,child3.attrib,child3.text)