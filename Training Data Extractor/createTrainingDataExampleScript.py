import createTrainingData

#how decompile a .replay file into .json format, save it locally(optional) returns extracted game frames data and controls:

extractedGameStatesAndControls = createTrainingData.convert_replay_to_game_frames("PATH TO DATA",save_json = False)



#how to extract game frames data and controls from a previously decompiled .json file:

createTrainingData.createAndSaveReplayTrainingDataFromJSON("PATH TO DATA", outputFileName = "exampleTrainingData.pbz2")


#how to load the data from a previously saved .pbz2 file:

gameData = createTrainingData.loadSavedTrainingData("exampleTrainingData.pbz2")


#uncomment below code and replace dummy arg with the path to a valid previously saved training data file. Run to see frame data format

# gameData = createTrainingData.loadSavedTrainingData("insert valid path to saved training data")
print(f"This variable contains data for {len(gameData)} game frames in addition to controller input data")
print(gameData[500]["GameState"])
print(gameData[500]["PlayerData"][0])

