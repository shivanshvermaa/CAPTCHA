import os
import cv2 as cv
from lxml import etree
import xml.etree.cElementTree as ET

def write_xml(folder,img, save_dir, character):
    "function to create the xml files for the images"
    
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
        
    image = cv.imread(img)
    height,weight,depth = image.shape
    
    
    annotation  = ET.Element('annotation')
    ET.SubElement(annotation,'folder').text = folder
    ET.SubElement(annotation,'filename').text = img
    ET.SubElement(annotation,'segmented').text = '0'
    
    size = ET.SubElement(annotation,'size')
    ET.SubElement(size,'height').text = str(height)
    ET.SubElement(size,'weight').text = str(weight)
    ET.SubElement(size,'depth').text = str(depth)
    
    ob = ET.SubElement(annotation,'object')
    ET.SubElement(ob,'name').text= str(character)
    ET.SubElement(ob,'pose').text= 'Unspecified'
    ET.SubElement(ob,'truncated').text= '0'
    ET.SubElement(ob,'difficult').text= '0'
    
    bbox =ET.SubElement(ob,'bndbox')
    
    ET.SubElement(bbox,'xmin').text = str(6)
    ET.SubElement(bbox,'ymin').text = str(6)
    ET.SubElement(bbox,'xmax').text = str(122)
    ET.SubElement(bbox,'ymax').text = str(122)
    
    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root,pretty_print=True)
    save_path = os.path.join(save_dir, img.replace('png', 'xml'))
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)
        
        
        
save_dir = "annotations"

count = 0 
p =  65

#CHANGE THE WORKPATHS AND DIRECTORIES FOR THE FONT PATH
for i in range(11,37):
    workPath = "F:\\Datasets\\EnglishFnt\\English\\Fnt\\"
    folder ="Sample{0:03}\\img{0:03}".format(i)
    
    
    for j in range(1,1017):
        image="-0{0:04}.png".format(j)        
        #print(workPath+folder+image)
        
        if ( i<= 10):
            write_xml(workPath+folder,workPath+folder+image,save_dir,i-1)
            
        if ( i>10 ):
            write_xml(workPath+folder,workPath+folder+image,save_dir,chr(p)) 
    
    if( i >10 ):
        print ( " DONE FOR  : "+  chr(p) )
        p += 1
            
            
    
    
    