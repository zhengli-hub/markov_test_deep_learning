from markov_test.REAL import *
import argparse
import pandas as pd
import numpy as np
import tensorflow as tf
import os
import sys

parser = argparse.ArgumentParser(description="mdn")
parser.add_argument("-L", "--L", type=int, default=3)
parser.add_argument("-B", "--B", type=int, default=1000)
parser.add_argument("-M", "--M", type=int, default=100)
parser.add_argument("-Q", "--Q", type=int, default=10)
parser.add_argument("-lr", "--lr", type=float, default=0.005)
parser.add_argument("-dim", "--dim", type=int, default=0)
parser.add_argument("-num_h", "--num_h", type=int, default=40)
parser.add_argument("-n_iter", "--n_iter", type=int, default=6000)
parser.add_argument("-file_n", "--file_n", type=int, default=0)
parser.add_argument("-rep", "--rep", type=int, default=0)
args0 = parser.parse_args()

string = f"mdn_real_ngsim1s_{args0.file_n}_dg_{args0.dim}_rep_{args0.rep}"

series = np.load(f"data_0507/ngsim_data/output_data/no_test/1s_npy/{args0.file_n}")


class Setting:
    def __init__(self):
        self.T = series.shape[0]
        self.x_dims = series.shape[1]
        self.L = args0.L
        self.B = args0.B
        self.M = args0.M
        self.Q = args0.Q
        self.lr = args0.lr
        self.dim = args0.dim
        self.show = False
        self.h1 = args0.num_h
        self.k1 = None
        self.n1 = args0.n_iter
        self.h2 = args0.num_h
        self.k2 = None
        self.n2 = args0.n_iter
        self.h3 = args0.num_h
        self.k3 = None
        self.n3 = args0.n_iter
        self.h4 = args0.num_h
        self.k4 = None
        self.n4 = args0.n_iter
        self.h5 = args0.num_h
        self.k5 = None
        self.n5 = args0.n_iter
        self.h6 = args0.num_h
        self.k6 = None
        self.n6 = args0.n_iter
        self.cv_numk = [1, 3, 5, 7]


config = Setting()

pvalue_ls = []
config.test_lag = int(config.dim + 1)
print("Num GPUs Available: ", len(tf.config.list_physical_devices("GPU")))
tf.debugging.set_log_device_placement(True)


k_forward, k_backward = real_cv(config, series)
config.k1 = k_forward
config.k2 = k_forward
config.k3 = k_forward
config.k4 = k_backward
config.k5 = k_backward
config.k6 = k_backward
pvalue = real(config, series)
pvalue_ls.append(pvalue)
np.save("result/" + string, pvalue_ls)
print("Result for ", string, " is ", pvalue_ls)
