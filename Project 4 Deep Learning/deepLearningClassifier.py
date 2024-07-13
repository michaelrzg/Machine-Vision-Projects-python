# Michael Rizig
# Project 4: Deep Learing for Classification
# 001008703
# File 1: deepLearingClassifier.py
# 7/12/2024

#import Alexnet and other tools
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import AlexNet
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.optimizers import SGDimport 
from skimage import io
import os

#Prepare Data:

# Define data generator (from slides)
datagen = ImageDataGenerator(
rescale=1./255,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
validation_split=0.3) # Split data into training and validation

# Load and prepare data
data_dir = 'Train/' # Path to your data folder
batch_size = 32
train_generator = datagen.flow_from_directory(
data_dir,
target_size=(227, 227),
batch_size=batch_size,
class_mode='categorical',
subset='training') # Use 70% of data for training
val_generator = datagen.flow_from_directory(
data_dir,
target_size=(227, 227),
batch_size=batch_size,
class_mode='categorical',
subset='validation') # Use 30% of data for validation
#create groupings for labels
nonDRLabels = []
DRLabels = []

#retreive labels from title of each image
labels = os.listdir('Train/')   

#seperate id from label and pass into correct group
for s in labels:
    tag = s.split('-')[1]
    if tag == '0.jpg':
        nonDRLabels.append(s)
    elif tag == '2.jpg' or tag == '3.jpg':
        DRLabels.append(s)

print(len(nonDRLabels))
print(len(DRLabels))
#load images into memory:
#create list for image objects:
nonDRImages = []
DRImages = []

#load images into list
for s in nonDRLabels:
    nonDRImages.append(io.imread(f'Train/{s}'))

for s in DRLabels:
    DRImages.append(io.imread(f'Train/{s}'))

#ensure loading was successful:
assert len(nonDRImages) == len(nonDRLabels) and len(DRImages) == len(DRLabels)

print(nonDRImages[0].shape)

#repeat for test data:

testLabels = os.listdir('Test/')

nonDRTest = []
DRTest = []

for label in testLabels:
    tag = label.split('-')[1]
    if tag == '0.jpg':
        nonDRTest.append(io.imread(f'Test/{label}'))
    elif tag == '2.jpg' or tag == '3.jpg':
        DRTest.append(io.imread(f'Test/{label}'))



#load Alexnet 
pretrained = AlexNet.pretrained(weights='imagenet',include_top=False, input_shape=(1028,1062,3))

for layer in pretrained.layers:
    layer.trainable = False

newModel = AlexNet.Sequential()

newModel.add(pretrained)

newModel.add(AlexNet.Flatten())
newModel.add(AlexNet.Dense(256, activation='relu'))
newModel.add(AlexNet.Dropout(0.5))
newModel.add(AlexNet.Dense(10, activation='softmax')) # Assuming 10 classes
# Compile the newModel
newModel.compile(optimizer=SGD(lr=0.001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])
# Train the newModel
history = newModel.fit(
AlexNet.train_generator,
steps_per_epoch=len(AlexNet.train_generator),
epochs=5,
validation_data=AlexNet.val_generator,
validation_steps=len(AlexNet.val_generator))
# Save the trained newModel
newModel.save('alexnet_transfer_learning.h5')
