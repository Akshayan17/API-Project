import matplotlib.pyplot as plt
import numpy as np
import mplcursors

class Mathplotlib:
    def plot_graph(self, x_values, y_values, x_label, y_label, sorted_movies):
        plt.close('all')  # Close any existing figures
        
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(x_values, y_values, c='blue', marker='o')

        # Calculate and display correlation
        corr_coef = np.corrcoef(x_values, y_values)[0, 1]
        ax.text(0.05, 0.95, f'Correlation: {corr_coef:.2f}', 
                transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=0.5))

        # Add trendline
        slope, intercept = np.polyfit(x_values, y_values, 1)
        x_line = np.array([min(x_values), max(x_values)])
        ax.plot(x_line, slope * x_line + intercept, 'r-', label='Best Fit Line')

        # Labels and title
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(f"{y_label} vs {x_label}")
        ax.legend()

        # Interactive hover labels
        cursor = mplcursors.cursor(scatter, hover=True)
        @cursor.connect("add")
        def on_hover(sel):
            idx = sel.index
            sel.annotation.set_text(
                f'{sorted_movies[idx]}\n{x_label}: {x_values[idx]:.1f}\n{y_label}: {y_values[idx]:.1f}'
            )

        plt.tight_layout()
        plt.show(block=True)  # Force the window to stay open