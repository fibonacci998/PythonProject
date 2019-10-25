import numpy as np
import os
from math import log
from math import sqrt
import graphlab
PATH_TRAIN = os.path.join("dataset", "kc_house_train_data.csv")
PATH_TEST = os.path.join("dataset", "kc_house_test_data.csv")
sales = graphlab.SFrame('kc_house_data.gl/')
def load_data():
    train_data, test_data = sales.random_split(.8, seed=0)
    return (train_data, test_data)
def get_residual_sum_of_squares(model, data, outcome):
    # First get the predictions
    predictions = model.predict(data)
    # Then compute the residuals/errors
    residuals = outcome - predictions
    # Then square and add them up
    RSS = (residuals * residuals).sum()
    return(RSS)

def get_numpy_data(data_sframe, features, output):
    data_sframe['constant'] = 1
    features = ['constant'] + features

    features_sframe = data_sframe[features]

    features_matrix = features_sframe.to_numpy()

    output_sarray = data_sframe[output]

    output_array = output_sarray.to_numpy()
    return(features_matrix, output_array)
def predict_output(feature_matrix, weights):
    predictions = np.dot(feature_matrix, weights)
    return(predictions)
def feature_derivative(errors, feature):
    derivative = 2*np.dot(errors, feature)
    return(derivative)

def regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance):
    converged = False
    weights = np.array(initial_weights) # make sure it's a numpy array
    while not converged:
        # compute the predictions based on feature_matrix and weights using your predict_output() function
        predictions = predict_output(feature_matrix, weights)
        # compute the errors as predictions - output
        errors = predictions - output
        gradient_sum_squares = 0 # initialize the gradient sum of squares
        # while we haven't reached the tolerance yet, update each feature's weight
        for i in range(len(weights)): # loop over each weight
            # Recall that feature_matrix[:, i] is the feature column associated with weights[i]
            # compute the derivative for weight[i]:
            derivative = feature_derivative(errors, feature_matrix[:, i])
            # add the squared value of the derivative to the gradient magnitude (for assessing convergence)
            gradient_sum_squares += (derivative**2)
            # subtract the step size times the derivative from the current weight
            weights[i] -= (step_size * derivative)
        # compute the square-root of the gradient sum of squares to get the gradient matnigude:
        gradient_magnitude = sqrt(gradient_sum_squares)
        if gradient_magnitude < tolerance:
            converged = True
    return(weights)