from DirectoryUtils import ExtractingFiles
from ReadTextFile import TextExtraction
from DataProcessing import ImagePreProcessing
import cv2 as cv
import glob
import os

image = ImagePreProcessing()
training_classification = image.getClassifiedCroppedImageData()
print("training_classification")
print(training_classification)
training_bbox = image.getTrainingSetForBoundingBox()
print("training_bbox")
print(training_bbox)

    
    



