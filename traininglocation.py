
import tensorflow as tf
import pandas as pd 
from IPython.display import display
from Formatinput import *
from Datavisualizer import *

tf.debugging.set_log_device_placement(True)



training_data = pd.read_hdf("C:\\Users\\vansh\\Desktop\\Rocketleaguebot\\ReplayModels-master\\ReplayDataProcessing\\RANKED_DUELS\Datasets\\1400-1499\\43_games-18_pcols-17_gcols.h5",index_col = 0)
print(training_data.tail(5))
print(training_data.shape)
columnnames = training_data.columns.values
list_column = list(columnnames)
print(training_data.dtypes)
"""

for i in range(len(list_column)):
    print(list_column[i])

see_data = Datavisualize(training_data)
see_data.correlation_matrix()

"""
