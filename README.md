# Deep-learning-Rocket-league-bot

A Rocket League Bot which uses data to train a Neural Network to play the Game. I am currently working on teaching the robot using Reinforcement learning which has been more succesfull in the past. This project is very interesting and I am planning on commiting the data visualization file I used while working.

This project is unique in the way it trains the network. The network takes into the position of the ball(X,Y,Z rotation and the axis), position of the user(X,Y,Z rotation and the axis).Previous projects have failed to account for this.

## Usage

## Step 1: Download Replays 
In 
```downloadreplays.py``` enter your API key from https://ballchasing.com/ . Change the number of Replays to download in the variable on top. Configure the config file to download the file.

## Step 2: Download the custom Carball package

I have customized the Carball package to process the replay files successfully. So paste the file in your python environment. ( Uploading soon)

## Step 4: Process the data using Process Replays folder 

Process the data using the ```newtrainingdata.py```

## Step 5: Customize ```botnetwork.py``` 

Modify the network based on how the data is distributed.

## Step 6: Run ```trainnetwork.py```

Run this file to train the network. Make sure you link the path to data and pre process the data using the file in Process Replays it converts replay data to JSON format



## Example 

https://user-images.githubusercontent.com/68335743/139625631-a3b594a0-df2a-4492-be87-b2d2e610e069.mp4

