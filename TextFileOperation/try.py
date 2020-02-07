from DirectoryUtils import ExtractingFiles
from ReadTextFile import TextExtraction
import tensorflow as tf
extraction = ExtractingFiles()

files = extraction.extractTextFileNames()
text = TextExtraction(files[0])
print(text.textExtraction())