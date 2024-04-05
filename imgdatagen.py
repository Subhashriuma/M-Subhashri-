import matplotlib
matplotlib.use ("Agg")
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler
from keras.optimizers import Adagrad
from keras.utils import np_utils
from sklearn.metrics import classification_report
from sklearn.metrics import confusion matrix
from cancernet.cancernet import CancerNet
from cancernet import config
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import os
NUM EPOCHS-40; INIT_LR-le-2: BS-32
trainPaths-list (paths.list_images (config.TRAIN_PATH}}
lenTrain-len (trainPaths)
lenVal-len (list (paths.list_images (config.VAL_PATH)))
lenTest-len (list (paths.list_images (config.TEST_PATH)))
trainLabels=[int (p.split (os.path.sep) [-2]) for p in trainPaths]
trainLabels-np_utils.to_categorical (trainLabels)
classTotals-trainLabels.sum (axis=0)
classWeight-classTotals.max()/classTotals
trainAug ImageDataGenerator(
rescale=1/255.0,
rotation_range=20,
zoom range-0.05,
width shift range 0.1,
height shift_range=0.1,
shear_range=0.05,
horizontal flip-True,
vertical flip-True,
fill_mode="nearest")
valAug ImageDataGenerator (rescale=1 / 255.0)
