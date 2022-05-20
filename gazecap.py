import scipy.io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import pandas as pd
import json


motion_path = "./GazeCapture/00002/motion.json"

with open(motion_path, 'r') as file:
    data = json.load(file)
    # print(type(data))
    # print(data)

data[0].