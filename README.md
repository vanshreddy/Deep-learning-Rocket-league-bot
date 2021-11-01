# Deep-learning-Rocket-league-bot

A Rocket League Bot which uses data to train a Neural Network to play the Game. I am currently working on teaching the robot using Reinforcement learning which has been more succesfull in the past. This project is very interesting and I am planning on commiting the data visualization file I used while working.

## Usage

##Step 1: Download Replays 
In 
```downloadreplays.py``` enter your API key from https://ballchasing.com/ . Change the number of Replays to download in the variable on top. Configure the config file to download the file.

##Step 2: Download the custom Carball package

I have customized the Carball package to process the replay files successfully. So paste the file in your python environment. ( Uploading soon)

##Step 4: Process the data using the training data extractor 

Process the data using the ```createTrainingDataExampleScript.py```

##Step 5: Customize ```botnetwork.py``` 

Modify the network based on how the data is distributed.

##Step 6: Run ```trainnetwork.py```

Run this file to train the network. Make sure you link the path to data.



