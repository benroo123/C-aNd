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

if __name__ == "__main__":
