from DirectoryUtils import ExtractingFiles
from ReadTextFile import TextExtraction
extraction = ExtractingFiles()

files = extraction.extractTextFileNames()
text = TextExtraction(files[0])
print(text.textExtraction())