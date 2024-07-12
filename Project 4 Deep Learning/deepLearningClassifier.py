# Michael Rizig
# Project 4: Deep Learing for Classification
# 001008703
# File 1: deepLearingClassifier.py
# 7/12/2024

#import Alexnet and other tools
from alexnet_pytorch import AlexNet
import os
from skimage import io

#Prepare Data:

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

#ensure images are 1062x1028 and not 227x227:
assert nonDRImages[0].shape == (1028,1062,3)

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
pretrained = AlexNet(weights='imagenet',include_top=False, input_shape=(1028,1062,3))

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
