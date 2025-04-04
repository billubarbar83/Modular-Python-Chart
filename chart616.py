import os
import matplotlib.pyplot as plt
from chart_handler.base_handler import BaseChart


class Chart616(BaseChart):
    def plot(self):
        # Load all 5 DataFrames
        df_excessive = self.dataframes["616_0.csv"]
        df_total_stock = self.dataframes["616_1.csv"]
        df_cogs = self.dataframes["616_2.csv"]
        df_turnover = self.dataframes["616_3.csv"]
        df_excessive_turnover = self.dataframes["616_4.csv"]

        # Titles and labels
        column_titles = ["excessive", "Total_stock", "COGS", "turn_over", "excessive turn over"]
        dfs = [df_excessive, df_total_stock, df_cogs, df_turnover, df_excessive_turnover]
        colors = ["mediumturquoise", "cornflowerblue", "plum", "slateblue", "lightgray"]
        value_columns = [df.columns[1] for df in dfs]

        # Create subplots
        self.fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(18, 8))
        self.ax1 = axes[0]  # Assign first axis for title if needed

        for ax, df, color, title, value_col in zip(axes, dfs, colors, column_titles, value_columns):
            # Plot horizontal bar
            ax.barh(df["item"], df[value_col], color=color, edgecolor="black")

            # Annotate each bar with its value
            for index, value in enumerate(df[value_col]):
                ax.text(value, index, f"{round(value)}", va="center", fontsize=7)

            # Title and style
            ax.set_title(title, fontsize=12, color="red")
            ax.set_yticks(range(len(df)))
            ax.set_yticklabels(df["item"], fontsize=8)
            ax.invert_yaxis()  # Top to bottom

            # Hide x-axis ticks for compactness
            ax.tick_params(axis="x", labelsize=7)
            ax.tick_params(axis="y", labelsize=8)

        # Add a big label on the left for items
        self.fig.text(0.01, 0.5, "item_01-30", va="center", rotation=90, fontsize=16, color="red")

        # Top center title
        self.fig.suptitle(
            "Top 30 Items by Excessive Inventory (Over 6 months)\nSelected Date: 2025-01-20",
            fontsize=12
        )

        plt.tight_layout()
        plt.subplots_adjust(top=0.88)

    def save_chart(self, save_dir, chart_type):
        output_path = os.path.join(save_dir, f"{chart_type}.png")
        self.fig.tight_layout()
        self.fig.savefig(output_path)
        return output_path
