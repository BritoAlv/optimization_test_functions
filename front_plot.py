import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
from bounded_function import BoundedFunction
from alg import Alg

def front_plot( alg : Alg, bf : BoundedFunction):
    # Initial setup
    x = np.linspace(bf.range_x1[0], bf.range_x1[1])
    y = np.linspace(bf.range_x1[0], bf.range_x2[1])
    alg.set_range(bf.range_x1, bf.range_x2)
    X, Y = np.meshgrid(x, y)
    # Compute the function values
    Z = bf.f(X, Y)
    fig, ax = plt.subplots(figsize=(10, 10))
    contour = ax.contour(X,Y,Z, levels=50, cmap = "plasma")
    scatter = ax.scatter([], [] , color='r', s = 10, zorder = 10)
    ax.set_title(f"Interactive Plot of Algorithm {alg.name} with Function {bf.name}")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    colorbar = plt.colorbar(contour, ax=ax)
    colorbar.set_label('Function Value')

    # Function to update scatter data
    def update_scatter():
        global scatter_data
        alg.update_points(bf)
        points = alg.get_points()
        scatter_data = np.array([[p[0] for p in points], [p[1] for p in points]])
        scatter.set_offsets(scatter_data.T)

    # Button callback function
    def button_callback(event):
        update_scatter()
        fig.canvas.draw_idle()

    # Add button widget
    ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])
    button = Button(ax_button, 'Update Scatter')
    button.on_clicked(button_callback)


    # Show the plot
    plt.show()