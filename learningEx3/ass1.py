import numpy as np
import pandas as pd
import os
PATH_TRAIN = os.path.join("dataset", "kc_house_train_data.csv")
PATH_TEST = os.path.join("dataset", "kc_house_test_data.csv")

def load_house_data(path):
    return pd.read_csv(path)

def simple_linear_regression(input_feature, output):
    sum_y = sum(output)
    sum_x = sum(input_feature)
    sum_yx = sum(output*input_feature)
    sum_xx = sum(input_feature**2)
    n = len(output)
    slope = (sum_yx - ((sum_y * sum_x) / n)) / (sum_xx - ((sum_x ** 2) / n))
    intercept = (sum_y / n) - slope * (sum_x / n)
    return (intercept, slope)

def get_regression_predictions(input_feature, intercept, slope):
    return(intercept + slope*input_feature)

def get_residual_sum_of_squares(input_feature, output, intercept,slope):
    y_hat = intercept + slope * input_feature
    return (sum((output - y_hat) ** 2))

def inverse_regression_predictions(output, intercept, slope):
    return((output - intercept)/slope)