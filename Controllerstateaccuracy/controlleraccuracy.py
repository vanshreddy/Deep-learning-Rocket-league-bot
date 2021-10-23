from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
from carball.controls.controls import ControlsCreator
import math
import os
import json
import carball
import pickle
import bz2
import sys



    

if __name__ == "__main__":
    _json = carball.decompile_replay("PATH TO ")

    game = Game()
    game.initialize(loaded_json=_json)

    analysis_manager = AnalysisManager(game)
    analysis_manager.create_analysis()
    dataframe = analysis_manager.get_data_frame()
    dataframeun = dataframe.loc[:,("TEAM NAME","steer")]
    print(type(dataframe))
    print(dataframe.loc[1, ('TEAM NAME', 'ping')])
    print(dataframeun.head())  

    print("Done")



    non_player = ['ball_pos_x', 'ball_pos_y', 'ball_pos_z', 'ball_rot_x', 'ball_rot_y', 'ball_rot_z',
                  'ball_vel_x', 'ball_vel_y', 'ball_vel_z', 'ball_ang_vel_x', 'ball_ang_vel_y', 'ball_ang_vel_z',
                  'game_seconds_remaining', 'game_goal_number']
    z_zero = ['z_0_pos_x', 'z_0_pos_y', 'z_0_pos_z', 'z_0_rot_x', 'z_0_rot_y', 'z_0_rot_z',
              'z_0_vel_x', 'z_0_vel_y', 'z_0_vel_z', 'z_0_ang_vel_x', 'z_0_ang_vel_y', 'z_0_ang_vel_z','z_0_throttle',
              'z_0_steer','z_0_handbrake','z_0_boost', 'z_0_boost_active', 'z_0_jump_active', 'z_0_double_jump_active', 'z_0_dodge_active',
              'z_0_is_demo']