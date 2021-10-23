from os import walk
import csv
import sys


import keras
from keras import models, layers
import tensorflow as tf
import numpy
import math
import dask.dataframe
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime, timedelta
from Botnetwork import botNN
from keras import models, layers, Input, Model
import keras
import tensorflow as tf
import datetime




INPUT_ELEMENTS = 62
logDir ="logs\\"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

tbCallback = keras.callbacks.TensorBoard(logDir, histogram_freq=1)

data = pd.read_hdf(
"PATH TO DATA",    index_col=0)
print("g")
data.drop("game_seconds_remaining",axis=1,inplace = True)
data.drop("secs_to_goal",axis=1,inplace = True)
data.drop("next_goal_one",axis=1,inplace = True)
data.drop("score_zero",axis=1,inplace = True)
data.drop("score_one",axis=1,inplace = True)
data.drop("z_0_cjump",axis = 1,inplace = True)
data.drop("o_0_cjump",axis = 1,inplace = True)



input_state = []
boost_state = []
euler_state = []
jump_state = []
steer_state = []

for col in data.columns:
    if 'pos_x' in col:
        data[col] = data[col].divide(4096)
        input_state.append(col)
    if 'pos_y' in col:
        data[col] = data[col].divide(5120)
        input_state.append(col)
    if 'pos_z' in col:
        data[col] = data[col].divide(2044)
        input_state.append(col)
    if 'vel' in col:
        input_state.append(col)
        if 'ang_vel' in col:
            if 'ball' not in col:
                data[col] = data[col].divide(5.5)
        else:
                if 'ball' not in col:
                    data[col] = data[col].divide(2300)
                else:
                    data[col] = data[col].divide(6000)
    if 'cpitch' in col:
        euler_state.append(col)
        data[col] = data[col].divide((math.pi/2.0))
    if 'cyaw' in col:
        euler_state.append(col)
        data[col] = data[col].divide(math.pi)
    if 'croll' in col:
        euler_state.append(col)
        data[col] = data[col].divide(math.pi)
    if 'cthrottle' in col:
        steer_state.append(col)
    if 'csteer' in col:
        steer_state.append(col)
    if "boost" in col:
        if "c" not in col:
            boost_state.append(col)
    if "jump" in col:
        jump_state.append(col)

input_state = input_state[9:27]
jump_state = jump_state[2:4]
euler_state = euler_state[3:6]
boost_state = boost_state[-1]
steer_state = steer_state[2:4]


input_batch = data[input_state]
jump_batch = data[jump_state]
euler_batch = data[euler_state]
boost_batch = data[boost_state]
steer_batch = data[steer_state]
validationIndexStart = math.floor(input_batch.shape[0] * 0.8)

stateTensor = input_batch.to_numpy()
steerTensor = steer_batch.to_numpy()
eulerTensor = euler_batch.to_numpy()
jumpTensor = jump_batch.to_numpy()
boostTensor = boost_batch.to_numpy()

validationStates = stateTensor[validationIndexStart:]
validationSteer = steerTensor[validationIndexStart:]
validationEuler = eulerTensor[validationIndexStart:]
validationJump = jumpTensor[validationIndexStart:]
validationBoost = boostTensor[validationIndexStart:]

# remove validation for training sets
stateTensor = stateTensor[:validationIndexStart]
steerTensor = steerTensor[:validationIndexStart]
eulerTensor = eulerTensor[:validationIndexStart]
jumpTensor = jumpTensor[:validationIndexStart]
boostTensor = boostTensor[:validationIndexStart]



netBuilder = botNN(18)
model = netBuilder.buildModel()

history = model.fit(stateTensor,
                        [steerTensor, eulerTensor, jumpTensor, boostTensor],
                        epochs=5,
                        batch_size=2048,
                        validation_data=(
                        validationStates, [validationSteer, validationEuler, validationJump, validationBoost]), callbacks=[tbCallback]
                    )


model.save(logDir+'NNmodel')