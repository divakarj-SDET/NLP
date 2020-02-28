import os
import glob
import numpy as np
import pandas as pd

class TextExtraction:
    pathOfTextFile = None
    imageName = None
    
    @classmethod
    def __init__(self, textFileName):
        self.pathOfTextFile = os.getcwd()+"/Directory/trunk/Files/"+textFileName+".txt"
        
    def textExtraction(self):
        ds = pd.read_csv(self.pathOfTextFile,sep=",",header=None)
        columns = ds.columns.tolist()
        new_ds = ds.drop(columns=len(columns)-1)
        
        return new_ds.to_numpy()

    
    