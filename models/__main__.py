import datetime as dt
import glob
import pickle
import re
import string
import sys
import time
import warnings
from datetime import datetime
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.base import (
    BaseEstimator,
    TransformerMixin,
)
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    LabelEncoder,
    MinMaxScaler,
    StandardScaler,
    normalize,
)
from tqdm import tqdm

from sklearn.model_selection import cross_val_score

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score
import time
from sklearn.model_selection import KFold

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


key_features = [
    "CO(GT)_winsor",
    "PT08.S1(CO)_winsor",
    "PT08.S4(NO2)_winsor",
    "NO2(GT)_winsor" "T_winsor",
    "RH_winsor",
    "AH_winsor",
    "day_winsor",
    "year_winsor",
    "quarter_winsor",
    "weekday_winsor",
    "CO(GT)",
    "PT08.S1(CO)",
    "NO2(GT)",
    "PT08.S4(NO2)",
    "T",
    "RH",
    "AH",
    "day",
    "year",
    "quarter",
    "weekday",
]
