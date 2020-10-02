import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf 


tensor = tf.constant([5,2, 3])

print(tensor)
print(f'I am the argmax {tf.math.argmax(tensor)}')
print(type(int(tf.math.argmax(tensor))))
t = tensor.numpy() 

print(t)
print(t.argsort())