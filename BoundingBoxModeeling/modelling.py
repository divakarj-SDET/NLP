import tensorflow as tf
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.layers import Conv2D, Reshape
from keras import Model

class TrainModel:
    trainX = None
    trainY = None
    model = None
    @classmethod
    def __init__(self,train_X,train_y):
        self.trainX = train_X
        self.trainY = train_y
    
    def createModileNetModel(self,image_size, num_of_layers):
        self.model = MobileNet(input_shape=(image_size,image_size,num_of_layers),alpha=1.0,include_top=False)
        for layer in self.model.layers:
            layer.trainable = False
        # Add new top layer which is a conv layer of the same size as the previous layer so that only 4 coords of BBox can be output
        x = self.model.layers[-1].output
        x = Conv2D(4, kernel_size=4, name="coords")(x)
        # In the line above kernel size should be 3 for img size 96, 4 for img size 128, 5 for img size 160 etc.
        x = Reshape((4,))(x) # These are the 4 predicted coordinates of one BBox
        self.model = Model(inputs=self.model.input, outputs=x)
  
    def fitDataInModel(self):
        self.model.fit(self.trainX,self.trainY,epochs = 30,batch_size=32,verbose=1)
        self.model.save()