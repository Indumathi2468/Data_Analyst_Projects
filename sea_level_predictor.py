import pandas as pd
import matplotlib.pyplot as plti
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, color='red')

    # Second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, color='green')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()
