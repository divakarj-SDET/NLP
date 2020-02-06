import os
import glob
import numpy as np
import pandas as pd

class TextExtraction:
    pathOfTextFile = None
    imageName = None
    @classmethod
    def __init__(self, textFileName):
        self.pathOfTextFile = os.getcwd()+"/Directory/trunk/Resumes/"+textFileName+".txt"
        
    def __textExtraction(self):
        ds = pd.read_csv(self.pathOfTextFile,sep=",")
        numpyArray = ds.to_numpy()
        return numpyArray

    
    