import os.path
from os import path
import glob
print(path.exists(os.getcwd()+"/NLP/trunk/Resumes"))
print(glob.glob(os.getcwd()+"/NLP/trunk/Resumes/*")[1].split("\\")[-1])