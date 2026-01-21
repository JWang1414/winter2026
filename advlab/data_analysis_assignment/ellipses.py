import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# TODO:
# Define the distribution functions (Gaussian, lognormal etc)
# Plot the data
# Use curve_fit to determine which function matches
# Analyze with residuals, chi-squared, and covariance

MEASUREMENT_PATH = "advlab/data_analysis_assignment/measurements.csv"
UNCERTAINTY_PATH = "advlab/data_analysis_assignment/uncertainties.csv"

# Import data from CSV file
data = pd.read_csv(MEASUREMENT_PATH)
unc = pd.read_csv(UNCERTAINTY_PATH)

# Extract x and y data
x_data = data['x (units)'].values
y_data = data['y (units)'].values

x_unc = unc['x (units)'].values
y_unc = unc['y (units)'].values
