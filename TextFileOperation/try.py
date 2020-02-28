from DirectoryUtils import ExtractingFiles
from ReadTextFile import TextExtraction
import cv2 as cv

extraction = ExtractingFiles()

files = extraction.extractTextFileNames()

text = TextExtraction(files[0])
print(text.textExtraction())
print(text.textExtraction().head(1))
X1 = 0.321939*500
Y1 = 0.204554*500
X2 = 0.610003*500
Y2 = 0.203364*500
X3 = 0.611479*500
Y3 = 0.222373*500
X4 = 0.322607*500
Y4 = 0.223872*500
filename = "C:\\Users\\divakarjoshi\\Downloads\\0156b46f.jpeg"
unscaled = cv.imread(filename)
print(unscaled.shape)
image = cv.resize(unscaled, (500, 500))
color = (255,0,0)
image_contoured = cv.rectangle(image,(int(X1),int(Y1)),(int(X3),int(Y3)),(255,0,0),1)
cv.imshow("contoured_image",image_contoured)
cv.waitKey(0)
cropped = image[int(Y1):int(Y1)+(int(Y4)-int(Y1)),int(X1):int(X1)+(int(X2)-int(X1))]
cv.imwrite("image.png",cropped)