import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
import pickle
import seaborn as sns
import plotly_express as px
import matplotlib.pyplot as plt


train = pd.read_csv("data_titanic/train.csv")
test = pd.read_csv("data_titanic/test.csv")
gender_sub = pd.read_csv("data_titanic/gender_submission.csv")