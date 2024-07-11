from alexnet_pytorch import AlexNet

pretrained = AlexNet(weights='imagenet',include_top=False, input_shape=(1062,1028,3))

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
