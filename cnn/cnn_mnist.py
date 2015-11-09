# coding: utf-8

# Convolutional Neural Networkの勉強のため自作する

import numpy as np
import six
import matplotlib.pyplot as plt

# mnistの画像を表示する
def draw_digit(data):
    size = 28
    plt.figure(figsize=(2.5, 3))

    X, Y = np.meshgrid(range(size),range(size))
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]             # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(X, Y, Z)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

    plt.show()

def read_mnist_data():
  # すでにmnist.pklになっているデータを読み込む
  with open('mnist.pkl', 'rb') as mnist_pickle:
    mnist = six.moves.cPickle.load(mnist_pickle)
    
  # 画素値を[0.0, 1.0]に正規化する
  mnist['data'] = mnist['data'].astype(np.float32)
  mnist['data'] /= 255
  mnist['target'] = mnist['target'].astype(np.int32)
  
  # mnist.pklはトレーニングデータ60000枚，テストデータ10000枚の70000枚となっている．
  # それをトレーニングデータとテストデータに分ける
  N = 60000
  x_train, x_test = np.split(mnist['data'],   [N])
  y_train, y_test = np.split(mnist['target'], [N])
  N_test = y_test.size

  return x_train, x_test, y_train, y_test

# main
N = 60000
N_test = 10000
x_train, x_test, y_train, y_test = read_mnist_data()


