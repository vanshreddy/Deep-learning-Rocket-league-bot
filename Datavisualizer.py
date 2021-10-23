
import tensorflow as tf
import pandas as pd 
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
from Formatinput import *


def make_tensor(a):
    tf.tensor(a)

class DataVisualize:
    def __init__(self,class_input:InputFormat):
        self.input = class_input
    

    def correlation_matrix(self):
        plt.matshow(self.data.corr())
        plt.show()

    def get_tail(self, datapoints = 5):
        print(self.training_data.tail(datapoints))

    def get_shape(self):
        return self.training_data.shape
    
    def correlationmatrixheatmap(self):
        sns.heatmap(self.training_data.corr(),annot=True,linewidths=0.2)
        fig=plt.gcf()
        fig.set_size_inches(300,300)
        plt.show()
    
    def correlationmatrix(self):
        print(self.training_data.corr())
    
    #Does not work yet
    def pairplot(self):
        g = sns.pairplot(data=self.training_data, hue='Survived', palette = 'seismic',
                 size=5,diag_kind = 'kde',diag_kws=dict(shade=True),plot_kws=dict(s=10) )
        g.set(xticklabels=[])

    def get_info(self):
        return self.training_data.info()

    def checknull(self):
        print(self.training_data.isnull().sum())

