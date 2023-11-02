import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],
                df['CSIRO Adjusted Sea Level'],
                label='Sea Level Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    line1 = [slope * year + intercept for year in years]
    plt.plot(years, line1, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(
        recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years = range(2000, 2051)
    line2 = [slope * year + intercept for year in years]
    plt.plot(years, line2, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc=('upper left'))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
