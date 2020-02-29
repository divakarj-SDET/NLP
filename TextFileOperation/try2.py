from DataProcessing import ImagePreProcessing

image = ImagePreProcessing(os.getcwd()+"/Directory/trunk/Files/")
training_classification = image.getClassifiedCroppedImageData()
for index,row in training_classification.iterrows():
    print(row[0])
    break 
print("training_classification")
print(training_classification)
training_bbox = image.getTrainingSetForBoundingBox()
print("training_bbox")
print(training_bbox)

    
    



