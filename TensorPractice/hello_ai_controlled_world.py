"""
A Bigger Step Towards My Own Deep Learning Aspirations
...Get Some Decent Proficiency Towards This
...Cool Things To Learn
"""

import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # Squash CPU/GPU warnings

hello = tf.constant("Hello, Our AI Overlords!")
sess = tf.Session()
print(sess.run(hello))