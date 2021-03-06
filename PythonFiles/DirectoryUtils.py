import os
import glob

class ExtractingFiles:
    pathofDirectory = None
    listOfFiles = None
    
    @classmethod
    def __init__(self):
        self.pathofDirectory = os.getcwd()+"/Directory/trunk/Files/"
        self.listOfFiles = glob.glob(pathname=self.pathofDirectory+"*.txt")
        

    def __extractlistOfFiles(self):
        files = []
        for file in self.listOfFiles:
            files.append(file.split("\\")[-1])
        return files

    def extractTextFileNames(self):
        listOfFiles = self.__extractlistOfFiles()
        textFileNames=[]
        for file in listOfFiles:
            textFileNames.append(file.split(".")[-2])

        return textFileNames
        
    
