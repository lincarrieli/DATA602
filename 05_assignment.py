'''
Assignment #5
1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not 
    guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 07_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables unless stated to do so
7. Make sure your work is committed to your master branch in Github
Packages required:
pip install cloudpickle==0.5.6 (this is an optional install to help remove a deprecation warning message from sklearn)
pip install sklearn
'''
# core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts

# infra
import unittest

# ------ Place code below here \/ \/ \/ ------
# import plotly library and enter credential info here
import plotly.graph_objects as go


# ------ Place code above here /\ /\ /\ ------





# ------ Place code below here \/ \/ \/ ------
# Load datasets here once and assign to variables iris and boston

iris = ds.load_iris()
boston = ds.load_boston()

# ------ Place code above here /\ /\ /\ ------




# 10 points
def exercise01():
    '''
        Data set: Iris
        Return the first 5 rows of the data including the feature names as column headings in a DataFrame and a
        separate Python list containing target names
    '''

    # ------ Place code below here \/ \/ \/ ------
    iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df_first_five_rows = iris_df.head()
    target_names = list(iris.target_names)

    # ------ Place code above here /\ /\ /\ ------


    return df_first_five_rows, target_names

# 15 points
def exercise02(new_observations):
    '''
        Data set: Iris
        Fit the Iris dataset into a kNN model with neighbors=5 and predict the category of observations passed in 
        argument new_observations. Return back the target names of each prediction (and not their encoded values,
        i.e. return setosa instead of 0).
    '''

    # ------ Place code below here \/ \/ \/ ------
    KNN(n_neighbors = 5)
    new_observations = []
    iris_predictions = KNN.predict(new_observations)

    # ------ Place code above here /\ /\ /\ ------


    return iris_predictions

# 15 points
def exercise03(neighbors,split):
    '''
        Data set: Iris
        Split the Iris dataset into a train / test model with the split ratio between the two established by 
        the function parameter split.
        Fit KNN with the training data with number of neighbors equal to the function parameter neighbors
        Generate and return back an accuracy score using the test data was split out
    '''
    random_state = 21

    

    # ------ Place code below here \/ \/ \/ ------
    X_train, X_test, y_train, y_test = tts(X, y, split, random_state)
    KNN(neighbors)
    KNN.fit(X_train, y_train)
    y_pred = KNN.predict(X_test)
    knn_score = KNN.score(X_test, y_test)


    # ------ Place code above here /\ /\ /\ ------


    return knn_score

# 20 points
def exercise04():
    '''
        Data set: Iris
        Generate an overfitting / underfitting curve of kNN each of the testing and training accuracy performance scores series
        for a range of neighbor (k) values from 1 to 30 and plot the curves (number of neighbors is x-axis, performance score 
        is y-axis on the chart). Return back the plotly url.
    '''
    
    # ------ Place code below here \/ \/ \/ ------
    # plotly_overfit_underfit_curve_url = go.Figure()

    neighbors = np.arange(1, 30)
    test_accuracy = np.empty(len(neighbors))
    train_accuracy = np.empty(len(neighbors))

    for i, k in enumerate (neighbors):
        KNN(neighbors = K)
        KNN.fit(X_train, y_train)
        train_accuracy [i] = KNN.score(X_train, y_train)
        test_accuracy [i] = KNN.score(X_test, y_test)


    plt.plot(neighbors, test_accuracy, label = "test accuracy")
    plt.plot(neighbors, train_accuracy, label = "train accuracy")
    plt.legend()
    plt.xlabel("number of neighbors")
    plt.ylabel("performance score")


    # ------ Place code above here /\ /\ /\ ------


    return plotly_overfit_underfit_curve_url

# 10 points
def exercise05():
    '''
        Data set: Boston
        Load sklearn's Boston data into a DataFrame (only the data and feature_name as column names)
        Load sklearn's Boston target values into a separate DataFrame
        Return back the average of AGE, average of the target (median value of homes or MEDV), and the target as NumPy values 
    '''

    # ------ Place code below here \/ \/ \/ ------
    boston_df = pd.DataFrame(boston.data, columns = boston.feature_names)
    boston_target = pd.DataFrame(boston.target)
    average_age = boston_df["AGE"].mean()
    average_medv = boston_target.mean()
    medv_as_numpy_values = np.asarray(boston_target)
    # ------ Place code above here /\ /\ /\ ------


    return average_age, average_medv, medv_as_numpy_values

# 10 points
def exercise06():
    '''
        Data set: Boston
        In the Boston dataset, the feature PTRATIO refers to pupil teacher ratio.
        Using a matplotlib scatter plot, plot MEDV median value of homes as y-axis and PTRATIO as x-axis
        Return back PTRATIO as a NumPy array
    '''

    # ------ Place code below here \/ \/ \/ ------
    plt.scatter(boston_df.PTRATIO, boston_target)
    
    X_ptratio = np.asarray(boston_df.PTRATIO)

    # ------ Place code above here /\ /\ /\ ------


    return X_ptratio

# 20 points
def exercise07():
    '''
        Data set: Boston
        Create a regression model for MEDV / PTRATIO and display a chart showing the regression line using matplotlib
        with a backdrop of a scatter plot of MEDV and PTRATIO from exercise06
        Use np.linspace() to generate prediction X values from min to max PTRATIO
        Return back the regression prediction space and regression predicted values
        Make sure to labels axes appropriately
    '''

    # ------ Place code below here \/ \/ \/ ------
    reg_model = plt.plot(boston_df.PTRATIO, boston_target)
    plt.xlabel("PTRATIO")
    plt.ylabel("Median value of homes (MEDV")
    #m, b = np.polyfit(boston_df.PTRATIO, boston_target, 1)
    #plt.plot(boston_df.PTRATIO, m * boston_df.PTRATIO + b)
    PTRATIO_min = boston_df["PTRATIO"].min()
    PTRATIO_max = boston_df["PTRATIO"].max()
    prediction_space = np.linspace(PTRATIO_min, PTRATIO_max, 50)
    # ------ Place code above here /\ /\ /\ ------

    return reg_model, prediction_space


class TestAssignment7(unittest.TestCase):
    def test_exercise07(self):
        rm, ps = exercise07()
        self.assertEqual(len(rm),50)
        self.assertEqual(len(ps),50)

    def test_exercise06(self):
        ptr = exercise06()
        self.assertTrue(len(ptr),506)

    def test_exercise05(self):
        aa, am, mnpy = exercise05()
        self.assertAlmostEqual(aa,68.57,2)
        self.assertAlmostEqual(am,22.53,2)
        self.assertTrue(len(mnpy),506)
        
    def test_exercise04(self):
         print('Skipping EX4 tests')     

    def test_exercise03(self):
        score = exercise03(8,.25)
        self.assertAlmostEqual(exercise03(8,.3),.955,2)
        self.assertAlmostEqual(exercise03(8,.25),.947,2)
    def test_exercise02(self):
        pred = exercise02([[6.7,3.1,5.6,2.4],[6.4,1.8,5.6,.2],[5.1,3.8,1.5,.3]])
        self.assertTrue('setosa' in pred)
        self.assertTrue('virginica' in pred)
        self.assertTrue('versicolor' in pred)
        self.assertEqual(len(pred),3)
    def test_exercise01(self):
        df, tn = exercise01()
        self.assertEqual(df.shape,(5,4))
        self.assertEqual(df.iloc[0,1],3.5)
        self.assertEqual(df.iloc[2,3],.2)
        self.assertTrue('setosa' in tn)
        self.assertEqual(len(tn),3)
     

if __name__ == '__main__':
    unittest.main()