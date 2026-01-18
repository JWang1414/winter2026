import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gaussian(x, mu, sigma):
    """
    Computes a Gaussian distribution in the typical probability density form.
    """
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Load the saved samples
samples_A = np.load('temp_images/samples_A.npy')
samples_B = np.load('temp_images/samples_B.npy')

# Combine samples into a list for processing
samples_list = [np.array(samples_A), np.array(samples_B)]

# Normalize the samples
for i in range(len(samples_list)):
    samples_list[i] = samples_list[i] / np.linalg.norm(samples_list[i])

# Plot the histograms and fitted curves
plt.figure(figsize=(12, 5))
colors = ['blue', 'orange']
labels = ['Species A', 'Species B']

for i, samples in enumerate(samples_list):
    # Histogram
    counts, bin_edges = np.histogram(samples, bins=30, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    plt.subplot(1, 2, i + 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color=colors[i], label='Histogram')

    # Fit Gaussian
    mu_init = np.mean(samples)
    sigma_init = np.std(samples)
    popt, pcov = curve_fit(gaussian, bin_centers, counts, p0=[mu_init, sigma_init])
    mu_fit, sigma_fit = popt

    # Compute the optimized Gaussian curve
    x_fit = np.linspace(min(samples), max(samples), 200)
    y_fit = gaussian(x_fit, mu_fit, sigma_fit)

    # Determine the quality of the fit
    pcov = np.sqrt(np.diag(pcov))
    residuals = counts - gaussian(bin_centers, *popt)
    chi_squared = np.sum((residuals ** 2) / gaussian(bin_centers, *popt))
    dof = len(bin_centers) - len(popt)
    print(f'Fit results for {labels[i]}: mu = {mu_fit:.4e}, sigma = {sigma_fit:.4e}')
    print(f"Chi-squared = {chi_squared:.4f}, dof = {dof:.4f}, chi-squared/dof = {chi_squared/dof:.4f}")
    print(f"Parameter uncertainties: mu = {pcov[0]:.4e}, sigma = {pcov[1]:.4e}")
    print()

    # Plot the fitted curve
    plt.plot(x_fit, y_fit, color='red', linewidth=2, label='Fitted Gaussian')

    # Labels and title
    plt.title(f'Velocity Distribution of {labels[i]}')
    plt.xlabel('Velocity')
    plt.ylabel('Density')
    plt.legend()
    plt.grid()

# Adjust layout and show/save the plot
plt.tight_layout()
# plt.savefig('temp_images/final_velocity_distributions.png')
plt.show()

### Printed output from one sample:
# Fit results for Species A: mu = 5.0182e-06, sigma = 2.5171e-03
# Chi-squared = 0.4405, dof = 28.0000, chi-squared/dof = 0.0157
# Parameter uncertainties: mu = 5.7564e-06, sigma = 4.7001e-06

# Fit results for Species B: mu = 7.2971e-06, sigma = 2.5160e-03
# Chi-squared = 0.3657, dof = 28.0000, chi-squared/dof = 0.0131
# Parameter uncertainties: mu = 5.9599e-06, sigma = 4.8663e-06
