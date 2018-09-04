# -*- coding: utf-8 -*-
"""mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLWW03YileppDmlOfeWJaH6VZ0Zp02FO
"""

import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

plt.imshow(x_test[0])
plt.show()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer="adam",
             loss="sparse_categorical_crossentropy",
             metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5)

var_lost, var_acc = model.evaluate(x_test,y_test)
print(var_lost, var_acc)

prediction = model.predict([x_test])
print(prediction)



import numpy as np
print(np.argmax(prediction[5]))

plt.imshow(x_test[5])
plt.show