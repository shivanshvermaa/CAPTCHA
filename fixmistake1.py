import xml.etree.ElementTree as ET


def relabel(path):
    tree = ET.parse(path)
    root = tree.getroot()
    xml_string = (ET.tostring(root,encoding="utf8").decode('utf8'))
    xml_string.replace("weight","width")
    xml_string.replace("<?xml version='1.0' encoding='utf8'?>\n","")
    
    root = ET.fromstring(xml_string)
    tree = ET.ElementTree(root)
    tree.write(xml_string)
    
    with open( path , "w" ) as f:
        f.write(xml_str)
        
path = r"F:\dataset\annotations\000000.xml"
relabel(path)


'''
newroot = ET.fromstring(xml_string)
newroot.write(r"F:\dataset\annotations\000000.xml",encodiong='unicode')
print(xml_string)
'''