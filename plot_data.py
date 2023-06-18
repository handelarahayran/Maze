import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns


def plot_data(maze, delay):
    """
    Plots the maze in a heatmap graph using predefined colours and labels
    The method has been coded so that it can be used in a loop
    :param maze: The maze table to be visualised
    :param delay: An added delay between each visualisation (must be positive)
    """
    cmap_dict = {0: '#000e8c', 1: '#dbdbdb', 2: '#65ff4a', 3: '#ff0019', 4: '#45caff', 5: '#f8ff30'}
    cmap = ListedColormap([cmap_dict[i] for i in range(6)])
    plt.clf()
    ax = sns.heatmap(data=maze, linewidths=1, cmap=cmap, vmin=-0.5, vmax=5.5)
    colorbar = ax.collections[0].colorbar
    colorbar.set_ticklabels(['', 'Wall', 'Empty', 'Start', 'Goal', 'Searched', 'Path'])
    for spine in colorbar.ax.spines.values():
        spine.set_visible(True)  # show the border of the colorbar
    plt.tight_layout()
    plt.draw()
    plt.pause(delay)
