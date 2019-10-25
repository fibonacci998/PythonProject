import sys
import os
sys.path.append('D:\PythonProject\testAna2\venv\Lib\site-packages')
import graphlab
import matplotlib.pyplot as plt
PATH_TRAIN = os.path.join("data_new", "kc_house_data.csv")

def polynomial_sframe(feature, degree):
    # assume that degree >= 1
    # initialize the SFrame:
    poly_sframe = graphlab.SFrame()
    # and set poly_sframe['power_1'] equal to the passed feature
    poly_sframe['power_1'] = feature
    # first check if degree > 1
    if degree > 1:
        # then loop over the remaining degrees:
        for power in range(2, degree+1):
            # first we'll give the column a name:
            name = 'power_' + str(power)
            # assign poly_sframe[name] to be feature^power
            poly_sframe[name] = feature ** power
    return poly_sframe

def process_model(sales, power):
    poly1_data = polynomial_sframe(sales['sqft_living'], power)
    poly1_data['price'] = sales['price']
    print poly1_data
    model1 = graphlab.linear_regression.create(poly1_data, target='price', features=['power_1'], validation_set=None)
    model1.get("coefficients")
    plt.show()
    plt.plot(poly1_data['power_1'], poly1_data['price'], '.', poly1_data['power_1'], model1.predict(poly1_data), '-')

def main():
    tmp = graphlab.SArray([1., 2., 3.])
    tmp_cubed = tmp.apply(lambda x: x ** 3)
    print tmp
    print tmp_cubed
    print polynomial_sframe(tmp, 3)
    global sales, model1, model2, model3
    sales = graphlab.SFrame('kc_house_data.gl/')
    sales = sales.sort(['sqft_living', 'price'])
    # process_model(sales, 1)
    # process_model(sales, 2)
    # process_model(sales, 3)
    poly1_data = polynomial_sframe(sales['sqft_living'], 1)
    poly1_data['price'] = sales['price']
    print poly1_data
    model1 = graphlab.linear_regression.create(poly1_data, target='price', features=['power_1'], validation_set=None)
    print model1.get("coefficients")
    plt.plot(poly1_data['power_1'], poly1_data['price'], '.', poly1_data['power_1'], model1.predict(poly1_data), '-')
    plt.show()

    poly2_data = polynomial_sframe(sales['sqft_living'], 2)
    my_features = poly2_data.column_names()  # get the name of the features
    poly2_data['price'] = sales['price']  # add price to the data since it's the target
    model2 = graphlab.linear_regression.create(poly2_data, target='price', features=my_features, validation_set=None)
    print model2.get("coefficients")
    plt.figure()
    plt.plot(poly2_data['power_1'], poly2_data['price'], '.', poly2_data['power_1'], model2.predict(poly2_data), '-')
    plt.show()

    poly3_data = polynomial_sframe(sales['sqft_living'], 3)
    poly3_features = poly3_data.column_names()  # get the name of the features
    poly3_data['price'] = sales['price']  # add price to the data since it's the target
    model3 = graphlab.linear_regression.create(poly3_data, target='price', features=poly3_features, validation_set=None)
    print model3.get("coefficients")
    plt.figure()
    plt.plot(poly3_data['power_1'], poly3_data['price'], '.',
             poly3_data['power_1'], model3.predict(poly3_data), '-')

    poly15_data = polynomial_sframe(sales['sqft_living'], 15)
    poly15_features = poly15_data.column_names()  # get the name of the features
    poly15_data['price'] = sales['price']  # add price to the data since it's the target
    model15 = graphlab.linear_regression.create(poly15_data, target='price', features=poly15_features,
                                                validation_set=None)
    print model15.get("coefficients")
    plt.figure()
    plt.plot(poly15_data['power_1'], poly15_data['price'], '.',
             poly15_data['power_1'], model15.predict(poly15_data), '-')

    bigset_1, bigset_2 = sales.random_split(0.5, seed=0)
    set_1, set_2 = bigset_1.random_split(0.5, seed=0)
    set_3, set_4 = bigset_2.random_split(0.5, seed=0)
    set_1_coef = get_coef(set_1)
    print set_1_coef[set_1_coef['name'] == 'power_15']

def get_poly_model(set_data):
    poly15_data = polynomial_sframe(set_data['sqft_living'], 15)
    poly15_features = poly15_data.column_names()  # get the name of the features
    poly15_data['price'] = set_data['price']  # add price to the data since it's the target
    model15 = graphlab.linear_regression.create(poly15_data, target='price', features=poly15_features,
                                                validation_set=None)
    return poly15_data, model15


def get_coef(set_data):
    poly15_data, model15 = get_poly_model(set_data)
    return model15.get("coefficients")


def plot_fitted_line(set_data):
    poly15_data, model15 = get_poly_model(set_data)
    return plt.plot(poly15_data['power_1'], poly15_data['price'], '.',
                    poly15_data['power_1'], model15.predict(poly15_data), '-')
if __name__ == "__main__":
    main()