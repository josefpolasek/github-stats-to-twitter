import pandas as pd
import matplotlib.pyplot as plt
import calmap


def make_graph(contributions):
    # Create a DataFrame from the contributions data
    df = pd.DataFrame(contributions)
    # Convert the date column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    # Filter for the year 2024
    df_2024 = df[df['date'].dt.year == 2024]

    # Set the date as the index and sort the data
    df_2024.set_index('date', inplace=True)
    df_2024.sort_index(inplace=True)

    # Create a series with the counts
    events = pd.Series(df_2024['count'].values, index=df_2024.index)

    # Plot the calendar heatmap
    plt.figure(figsize=(20, 10))
    calmap.yearplot(events, year=2024, cmap='Greens')
    plt.title('Contributions in 2024')

    return plt
