import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet

#OPTIONS FOR LOADING THE YOLO MODELS
options = {"model": "cfg/yolo_custom.cfg", 
           "load": "bin/yolo.weights",
           "batch": 8,
           "epoch": 100,
           "gpu": 1.0,
           "train": True,
           "annotation": "./annotations/",
           "dataset": "./images/"
           }

tfnet = TFNet(options)

tfnet.train()   


# this line of code lets you save the built graph to a protobuf file (.pb)  
tfnet.savepb()

