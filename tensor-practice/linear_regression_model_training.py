# Full Machine Learning Program...

from __future__ import print_function
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print("is this the good stuff?".title()) # Script Title
sess = tf.Session()

# Model Parameters - The Variables are the Best Guesses we currently have
M = tf.Variable([.3], dtype=tf.float32) #  Best Guess we have for M
b = tf.Variable([-.3], dtype=tf.float32) #  Best Guess we have for b
x = tf.placeholder(tf.float32)
linear_model = M * x + b

# essentially, we are trying to fit M and b using a gradual (GPU) exhaustive approach method
# everything is lambda'd (building an abstract structure)
# ?(the computer's work is just to find values that fit the structure)?
y = tf.placeholder(tf.float32)

# loss
# not sure; tf.reduce_sum() is called reduce sum
loss = tf.reduce_sum(tf.square(linear_model - y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss) # We want to minimize loss here/ <Thinking About The Many Applications of Minimizer>

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
	sess.run(train, {x: x_train, y: y_train})

curr_M, curr_b, curr_loss = sess.run([M, b, loss], {x: x_train, y: y_train})
print("M: %s b: %s loss: %s"%(curr_M, curr_b, curr_loss))

# Line of best fit problem that is completely generalized
# Potential fitting of a parabola
# Generate some parabola data use this method and it would probably give me a rather useful answer...