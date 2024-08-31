import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
from plot.bounded_function import BoundedFunction
from plot.alg import Alg


def one_plot(algs: list[Alg], bf: BoundedFunction):
    # set interval the provided by function
    for alg in algs:
        alg.x1_range = bf.range_x1
        alg.x2_range = bf.range_x2
        alg.initialize_points()

    # Initial setup
    x = np.linspace(bf.range_x1[0], bf.range_x1[1], 500)
    y = np.linspace(bf.range_x2[0], bf.range_x2[1], 500)
    X, Y = np.meshgrid(x, y)
    # Compute the function values
    Z = bf.f(X, Y)
    fig, ax = plt.subplots(
        figsize= (10, 10)
    )
    contour = ax.contourf(X, Y, Z, levels=10, cmap="plasma")
    colours = random.sample(["b", "g", "r", "c", "m", "y", "k", "w"], k=len(algs))
    scatters = [
        ax.scatter([], [], color=colours[i], s=10, zorder=10) for i in range(len(algs))
    ]
    ax.set_title(f"Interactive Plot of Algorithms with Function {bf.name}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    colorbar = plt.colorbar(contour, ax=ax)
    colorbar.set_label("Function Value")
    """
    Pending to implement add a legend to this.
    """

    # Function to update scatter data
    def update_scatter():
        for i, alg in enumerate(algs):
            alg.update_points(bf)
            points = alg.get_points()
            scatter_data = np.array([[p[0] for p in points], [p[1] for p in points]])
            scatters[i].set_offsets(scatter_data.T)
            alg.log_state(bf)

    # Button callback function
    def button_callback(event):
        update_scatter()
        fig.canvas.draw_idle()

    # Add button widget
    ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])
    button = Button(ax_button, "Update Scatter")
    button.on_clicked(button_callback)
    # Show the plot
    plt.show()
