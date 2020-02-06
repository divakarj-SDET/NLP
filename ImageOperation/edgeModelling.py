import tensorflow
import numpy as np
from PIL import Image
from keras import Model
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, Callback
from keras.layers import Conv2D, Reshape
from keras.utils import Sequence
from keras.backend import epsilon

ALPHA = 1.0  # Width hyper parameter for MobileNet (0.25, 0.5, 0.75, 1.0). Higher width means more accurate but slower

IMAGE_SIZE = 128  # MobileNet takes images of size 128*128*3

EPOCHS = 10  # Number of epochs. I got decent performance with just 5.
BATCH_SIZE = 32  # Depends on your GPU or CPU RAM.

path_of_image = "C:\\Users\\divakarjoshi\\Desktop\\0156b46f.jpeg"

img = Image.open(path_of_image)
img = img.resize((IMAGE_SIZE, IMAGE_SIZE)) # Resize image
img = img.convert('RGB')

