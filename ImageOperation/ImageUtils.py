import DirectoryUtils.ExtractingFiles
import ReadTextFile.TextExtraction 
import cv2 as cv
import os
import glob
class Utils:
    imageName = None
    listOfFiles = None
    @classmethod
    
    def __init__(self,imageName):
        self.imageName = imageName
        self.listOfImageFiles = glob.glob(pathname=os.getcwd()+"/Directory/trunk/Files/"+ imageName+".*")

print("DOne")