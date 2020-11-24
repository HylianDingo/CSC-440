# imports
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
import csv


header = True
#number_vars = 9

def analysis(data_file, analysis_selection, dependent=0, independent=1):
    
    # Analsis Options:
    # "Linear", "Quadratic", "Cubic"
    
    # load data set
    dataframe = pd.read_csv(data_file)
            
    X = dataframe.iloc[:, dependent].values.reshape(-1, 1)
    Y = dataframe.iloc[:, independent].values.reshape(-1, 1)
    
    
    try:
        if analysis_selection == "Linear":
            model = LinearRegression()  # create object for the class
            model.fit(X, Y)  # perform linear regression
            
            Y_pred = model.predict(X)  # make predictions
            plt.scatter(X, Y)
            plt.plot(X, Y_pred, color='red')
            plt.show()
            r_sq = model.score(X, Y)
            
        elif analysis_selection == "Quadratic":
            polynomial_features = PolynomialFeatures(degree=2)
            x_poly = polynomial_features.fit_transform(X)
    
            model = LinearRegression()
            model.fit(x_poly, Y)
            y_poly_pred = model.predict(x_poly)
            plt.scatter(X, Y)
            plt.plot(X, y_poly_pred, color='red')
            plt.show()
            r_sq = model.score(x_poly, Y)
            
        else:
            polynomial_features= PolynomialFeatures(degree=3)
            x_poly = polynomial_features.fit_transform(X)
    
            model = LinearRegression()
            model.fit(x_poly, Y)
            y_poly_pred = model.predict(x_poly)
            plt.scatter(X, Y)
            plt.plot(X, y_poly_pred, color='red')
            plt.show()
            r_sq = model.score(x_poly, Y)
        
        # write results to csv file
        with open('results.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(["Results for: ", analysis_selection])
            filewriter.writerow(["Coefficient of Determination: ", r_sq])
            filewriter.writerow(["Intercept (Beta_0): ", model.intercept_[0]])
            for i in range(0, len(model.coef_)):
                s = "Slope (Beta_" + str(i+1) + "): "
                filewriter.writerow([s, model.intercept_[i]])
                
    except ValueError: 
        # write results to csv file
        with open('results.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(["Invalid data type in data set", ""])
            
    except:
        # write results to csv file
        with open('results.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(["An error occurred", ""])
    
    
analysis("gasturbine.csv", "Cubic", 4, 6)
        
    
    