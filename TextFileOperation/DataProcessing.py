from DirectoryUtils import ExtractingFiles
from ReadTextFile import TextExtraction
import cv2 as cv
import os
import glob
import pandas as pd
class ImagePreProcessing:
    image_size=500
    files = None
    image_boundingBox_dataframe = pd.DataFrame(columns = ['image','imageName'])

    @classmethod
    def __init__(self):
        extraction = ExtractingFiles()
        self.files = extraction.extractTextFileNames()

    def getTrainingSetForBoundingBox(self):
        image_DataFrame = pd.DataFrame(columns = ['Image','BoundingBoxMatrix'])
        
        for file in self.files:
            imagePath = glob.glob(pathname=os.getcwd()+"\\Directory\\trunk\\Files/"+ file+".*g")
            print(imagePath)
            unscaled = cv.imread(imagePath[0])
            scaledImage =cv.resize(unscaled, (self.image_size, self.image_size))
            textFile = TextExtraction(file)
            textFileDataWithBoxName = textFile.textExtraction()
            columns = textFileDataWithBoxName.columns.tolist()
            textFileDataWithoutBoxName = textFileDataWithBoxName.drop(columns=len(columns)-1)
            image_DataFrame = image_DataFrame.append({'Image':scaledImage,'BoundingBoxMatrix':textFileDataWithoutBoxName.to_numpy()*self.image_size},ignore_index=True)
        return image_DataFrame

    def getClassifiedCroppedImageData(self):
        i=0
        classified_image_dataset = pd.DataFrame(columns = ['Image','classification'])
        for file in self.files:
            imagePath = glob.glob(pathname=os.getcwd()+"\\Directory\\trunk\\Files/"+ file+".*g")
            print(imagePath)
            unscaled = cv.imread(imagePath[0])
            scaledImage =cv.resize(unscaled, (self.image_size, self.image_size))
            textFile = TextExtraction(file)
            textFileDataWithBoxName = textFile.textExtraction()
            #X1,Y1,X2,Y2,X3,Y3,X4,Y4 = None,None,None,None,None,None,None,None
            for index,row in textFileDataWithBoxName.iterrows():
                X1 = float(row[0])*self.image_size
                Y1 = float(row[1])*self.image_size
                X2 = float(row[2])*self.image_size
                Y2 = float(row[3])*self.image_size
                X3 = float(row[4])*self.image_size
                Y3 = float(row[5])*self.image_size
                X4 = float(row[6])*self.image_size
                Y4 = float(row[7])*self.image_size
                image_contoured = cv.rectangle(scaledImage,(int(X1),int(Y1)),(int(X3),int(Y3)),(255,0,0),1)
                #cv.imshow("contoured_image",image_contoured)
                cropped = scaledImage[int(Y1):int(Y1)+(int(Y4)-int(Y1)),int(X1):int(X1)+(int(X2)-int(X1))]
                classified_image_dataset = classified_image_dataset.append({'Image':cropped,'classification':row[8]},ignore_index=True)
            cv.imwrite("image{0}.png".format(i),image_contoured)
            i=i+1
        return classified_image_dataset