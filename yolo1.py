import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet


def showImage(image):
    cv.imshow('OUTPUT' ,image)  
    cv.waitKey(0)
    cv.destroyAllWindows()

#LOADING THE YOLO MODEL WEIGHTS AND CLASSES
options = {
    'model': r"F:\Work\Yolo\darkflow-master\cfg\yolo.cfg",
    'load': r"F:\Work\Yolo\darkflow-master\bin\yolov2.weights",
    'threshold': 0.5,
    'gpu': 1.0
}

options['model']= options['model'].encode('ascii','ignore').decode('utf-8')
options['load'] = options['load'].encode('ascii','ignore').decode('utf-8')
tfnet = TFNet(options)

#TESTING THE IMAGE
image = cv.imread("F:\\Work\\people.jpg" , cv.IMREAD_COLOR )
result = tfnet.return_predict(image)


#DRAWING THE BOUNDING BOXES FOR THE RESULTS
top =  (result[0]['topleft']['x'],result[0]['topleft']['y'])
bottom = (result[0]['bottomright']['x'],result[0]['bottomright']['y'])
label = result[0]['label']
imageResult = cv.rectangle(image, top, bottom, (0,255,0),7) #RECTANGLE
imageResult = cv.putText(imageResult,str(label),top,cv.FONT_HERSHEY_COMPLEX,1 , (0,0,0), 2)
imageResult = cv.cvtColor(imageResult, cv2.COLOR_BGR2RBG)
plt.imshow(imageResult)
plt.show()


#DRAWING THE BOXES FOR MULTIPLE IMAGES
top =[]
bottom = []
label = []

for i in range ( 0 , len(result) ):
    top.append((result[i]['topleft']['x'],result[i]['topleft']['y']))
    bottom.append((result[i]['bottomright']['x'],result[i]['bottomright']['y']))
    label.append(result[i]['label'])
    
    #ADDING THE BOXES TO THE RESULTING IMAGE
    imageResult = cv.rectangle(image,top[i],bottom[i],( int(np.random.randint(1,250,1)) ,int(np.random.randint(1,250,1)),int(np.random.randint(1,250,1))),7)
    imageResult = cv.putText(imageResult,str(label[i]) , top[i] , cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    imageresult = cv.cvtColor(imageResult,cv.COLOR_BGR2RGB)
    
showImage(imageResult)
    
#1I9SJTUVO0Q4


cv.imwrite("F:\\output.jpg" ,imageResult)
 
    
    
    
    
    
    
    
    