# Co-Author/ Learner: Nguyen Truong Thinh
# Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
#
# The helper functions
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set the plotting DPI settings to be a bit higher.
plt.rcParams['figure.figsize'] = [8.0, 5.0]
plt.rcParams['figure.dpi'] = 150


def train(x, y, iterations, lr):
    w = np.zeros((x.shape[1], 1))
    for i in range(iterations):
        w -= gradient(x, y, w) * lr
    return w


def sigmoid(z):
    """The logistic function: z = 1 / (1 + e^-z)"""
    return 1 / (1 + np.exp(-z))


def forward(x, w):
    wei_sum = np.matmul(x, w)
    return sigmoid(wei_sum)


def classify(x, w):
    return np.round(forward(x, w))


def lower_loss(x, y, w):
    y_hat = forward(x, w)
    first_term = y * np.log(y_hat)
    second_term = (1 - y) * np.log(1 - y_hat)
    return -np.average(first_term + second_term)


def gradient(x, y, w):
    return np.matmul(x.T, (forward(x, w) - y)) / x.shape[0]


def train_with_history(x, y, iterations, lr, precision, init_w, init_b):
    w, b = init_w, init_b

    previous_loss = loss(x, y, w, b)
    history = [[w, b, previous_loss]]
    for i in range(0, iterations):
        w_gradient, b_gradient = gradient_two_variables(x, y, w, b)
        w -= lr * w_gradient
        b -= lr * b_gradient

        c_loss = loss(x, y, w, b)
        history.append([w, b, previous_loss])

        if abs(c_loss - previous_loss) < precision:
            return w, b, history
        previous_loss = c_loss
    raise Exception("Couldn't converge within %d iterations" % iterations)


def gradient_two_variables(x, y, w, b):
    """ Calculate the gradient of the curve """
    w_gradient = 2 * np.average(x * (predict(x, w, b) - y))
    b_gradient = 2 * np.average(predict(x, w, b) - y)
    return w_gradient, b_gradient


def predict(x, w, b):
    return x * w + b


def loss(x, y, w, b):
    return np.average((predict(x, w, b) - y) ** 2)


def load_text_dataset(text_dataset):
    return np.loadtxt(text_dataset, skiprows=1, unpack=True)


def plot_the_chart(x, y, x_label, y_label, w, b):
    sns.set()
    plt.plot(x, y, "bo")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel(x_label, fontsize=30)
    plt.ylabel(y_label, fontsize=30)
    x_edge, y_edge = 50, 50
    plt.axis([0, x_edge, 0, y_edge])
    plt.plot([0, x_edge], [b, predict(x_edge, w, b)], linewidth=1.0, color="y")
    plt.show()
