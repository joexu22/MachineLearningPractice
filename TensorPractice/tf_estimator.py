"""
High-Level TensorFlow library
    Runs Training Loops
    Runs Evaluation Loops
    Manages Data Sets

Note: I don't acutally understand what is going on here...
    Feature Columns
    Estimators

If I where asked to do these calculations manually
I would not know where to start?...
Requires Further Investigations
"""

# Showing us a simplified linear regression program using TensorFlow
# Using numpy to load, manipulation, and preprocess data (numbers)
import numpy as np
import tensorflow as tf

# List Feature
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]
# Being a Good Tensor Programmer likey requires the ability to break down complex problems in matrix like "tensors"

# Linear Regression Estimator
estimator = tf.estimator.LinearRegressor(feature_columns = feature_columns)
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])
input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)

# We can invoke 1000 training steps by invoking the  method and passing the
# training data set.
estimator.train(input_fn=input_fn, steps=1000)

# Here we evaluate how well our model did.
train_metrics = estimator.evaluate(input_fn=train_input_fn)
eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
print("train metrics: %r"% train_metrics)
print("eval metrics: %r"% eval_metrics)