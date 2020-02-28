from DirectoryPath import FileDirectories
import glob
class Utils:
    imageName = None
    listOfFiles = None
    @classmethod
    
    def __init__(self,imageName):
        self.imageName = imageName
        self.listOfImageFiles = glob.glob(pathname=FileDirectories.pathOfImages+ imageName+".*")

