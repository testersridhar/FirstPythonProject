import xml.etree.ElementTree as ET

tree = ET.parse('Sample.xml')
my_root = tree.getroot()
for x in my_root[0]:
    print(x.tag)