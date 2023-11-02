import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')
df.index = pd.to_datetime(df.index)

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
            & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x=df.index, y='value', ax=ax)
    ax.set(xlabel='Date',
           ylabel='Page Views',
           title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.strftime('%Y')
    df_bar['month'] = df_bar.index.strftime('%B')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.groupby(['year', 'month'])['value'].mean().unstack().plot(kind='bar',
                                                                     ax=ax)
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend([
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ],
        title='Months')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    sns.boxplot(data=df_box,
                x='month',
                y='value',
                ax=axes[1],
                order=[
                    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'
                ])
    axes[0].set(xlabel='Year',
                ylabel='Page Views',
                title='Year-wise Box Plot (Trend)')
    axes[1].set(xlabel='Month',
                ylabel='Page Views',
                title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
