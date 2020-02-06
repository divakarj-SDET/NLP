import os
import glob

class ExtractingFiles:
    pathofDirectory = None
    listOfFiles = None
    if __init__(self):
        self.pathofDirectory = os.getcwd()+"/NLP/trunk/Resumes"
        self.listOfFiles = glob.glob(pathname=self.pathofDirectory+"/*")

    def __extractlistOfFiles():
        files = []
        for file in self.listOfFiles:
            files.append(file.split("\\")[-1])
        return files

    
        
