import tensorflow as tf
import numpy as np
import random
# import pytorch

# the structure of a neuron
# a = [x] * [w] + b

# Neuron as a class
class Neuron:
    def __init__(self, dimension):
        # self.dimension = dimension
        self.w = np.random.rand(dimension)
        self.b = random.random()


def train(ne: Neuron, lr, epoch, data, label):
    for e in epoch:
        for x, y in zip(data, label):
            pred = np.matmul(x, ne.w) + ne.b
            # The purpose of activation function is to introduce non-linearities into the network
            pred = tf.math.sigmoid(pred)
            # pred = tf.math.tanh(pred)
            # pred = tf.nn.relu(pred)
            # modify the weight and bias here depends on the type of learning
            if pred > y:
                pass
            else:
                pass


def predict(ne:Neuron, data):
    r = []
    for d in data:
        pred = np.matmul(d, ne.w) + ne.b
        r.append(pred)
    return r


#
class SimpleFeedbackLearning:
    def __init__(self, num):
        # num is the feature number given by each x
        self.w = np.random.rand(num)
        self.b = np.random.rand()

    @ staticmethod
    def step(x, theta=0.5):
        return x >= theta

    def train(self, x, xT, learningRate, iter):
        for t in range(iter):
            for xi, xt in zip(x, xT):
                a = np.matmul(xi, self.w) + self.b
                # output = np.dot(xi, self.w) + self.b

                # Can use without activation function here
                # y = stepf(a)
                #
                # if y == xt:
                #     continue
                # else:
                #     if y > xt:
                #         self.w -= learningRate * xi
                #         self.b -= learningRate * self.b
                #     else:
                #         self.w += learningRate * xi
                #         self.b += learningRate * self.b

                if a > xt:
                    self.w -= learningRate * xi
                    self.b -= learningRate * self.b
                else:
                    self.w += learningRate * xi
                    self.b += learningRate * self.b

    def predict(self, x):
        pred = []
        for e in x:
            pred.append(SimpleFeedbackLearning.step(np.matmul(e, self.w) + self.b))

        return pred


# simple dense layer with tensorflow
class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, in_d, out_d):
        super(MyDenseLayer, self).__init__()
        self.w = self.add_weight([in_d, out_d])
        self.b = self.add_weithgt([1, out_d])

    def call(self, inputs):
        z = tf.matmul(inputs, self.w) + self.b
        output = tf.math.sigmoid(z)
        return output

# loss function:

# gradient descent
# Initiate random weight
# Loop until converge:
#    compute gradient
#    update weight
# Return weight


def compute_loss(w):
    return loss

lr = 0.01
weights = tf.Variable([tf.random.normal()])

while True:
    with tf.GradientTape as g:
        loss = compute_loss(weights)
        gradient = g.gradient(loss, weights)

    weights = weights - lr * gradient
