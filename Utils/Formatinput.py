
import tensorflow as tf
import pandas as pd 
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf  
#import seaborn as sns
from sklearn.model_selection import train_test_split



def make_tensor(a):
    tf.tensor(a)


class InputFormat:
    def __init__(self,path: str):
        self.path = path
        self.training_data = pd.read_hdf(self.path,index_col = 0)
        self.ret = 0
    
    def get_dataframe(self):
        return self.training_data

    def get_head(self,datapoints = 5):
        print(self.training_data.head(datapoints))

    
    def get_inputlocation(self):
        mycar= self.training_data.loc[:, "z_0_pos_x":"z_0_ang_vel_z"]
        oppcar = self.training_data.loc[:, "o_0_pos_x":"o_0_ang_vel_z"]
        ballpos = self.training_data.loc[:, "ball_pos_x":"ball_ang_vel_z"]
        ret = pd.concat([oppcar,ballpos],axis = 1)
        self.ret = ret

    
    def keras_model(self):
        Yt_train= self.training_data.loc[:, "z_0_pos_x"].values
        Xt_train = self.ret.values
        target = self.training_data.pop('z_0_pos_x',"z_0_ang_vel_z")



        dataset = tf.data.Dataset.from_tensor_slices((self.ret.values, target.values))
        for feat, targ in dataset.take(5):
             print ('Features: {}, Target: {}'.format(feat, targ))

        print(type(dataset))
       # X_train, X_test, y_train, y_test = train_test_split(Xt_train,Yt_train, test_size = 0.3, random_state = 42)

        
        
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(128,activation = "relu"))
        model.add(tf.keras.layers.Dense(64,activation = "relu"))
        model.add(tf.keras.layers.Dense(32,activation = "relu"))
        model.add(tf.keras.layers.Dense(16,activation = "relu"))
        model.add(tf.keras.layers.Dense(8,activation = "relu"))
        model.add(tf.keras.layers.Dense(1,activation = "sigmoid"))

        model.add(tf.keras.layers.Dense(128,activation = "relu"))
        model.add(tf.keras.layers.Dense(64,activation = "relu"))
        model.add(tf.keras.layers.Dense(32,activation = "relu"))
        model.add(tf.keras.layers.Dense(16,activation = "relu"))
        model.add(tf.keras.layers.Dense(8,activation = "relu"))
        model.add(tf.keras.layers.Dense(1,activation = "sigmoid"))
        
        model.add(tf.keras.layers.Dense(128,activation = "relu"))
        model.add(tf.keras.layers.Dense(64,activation = "relu"))
        model.add(tf.keras.layers.Dense(32,activation = "relu"))
        model.add(tf.keras.layers.Dense(16,activation = "relu"))
        model.add(tf.keras.layers.Dense(8,activation = "relu"))
        model.add(tf.keras.layers.Dense(1,activation = "sigmoid"))
        opt = tf.keras.optimizers.Adam(learning_rate=0.01)

        model.compile(optimizer=opt,
              loss=tf.keras.losses.MSE,
              metrics=['accuracy'])
        
        model.fit(dataset,epochs = 20, verbose = 1)

        model.save("my_model")
        score = model.evaluate(X_test, y_test)
        print(score)
    
        
