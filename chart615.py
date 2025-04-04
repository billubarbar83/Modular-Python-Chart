import matplotlib.pyplot as plt
from chart_handler.base_handler import BaseChart


class Chart615(BaseChart):
    def plot(self):
        df_upper = self.dataframes["615_upper.csv"]
        df_lower = self.dataframes["615_lower.csv"]

        # Create the subplots
        self.fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16, 8), sharex=True)
        self.ax1 = ax1  # assign for reference in save_chart or title
        self.ax2 = ax2

        # Upper: Stacked bar chart (exceeded + within)
        ax1.bar(df_upper["date"], df_upper["within"], label="within", color="violet", zorder=2)
        ax1.bar(df_upper["date"], df_upper["exceeded"], bottom=df_upper["within"], label="exceeded", color="cornflowerblue", zorder=3)
        ax1.set_ylabel("stock_volume", color="red", fontsize=12)
        ax1.legend(loc="upper left")
        ax1.grid(True, which="both", axis="y", linestyle="--", zorder=1)

        # Upper chart annotations
        for i, (x, y) in enumerate(zip(df_upper["date"], df_upper["exceeded"])):
            total = df_upper["within"][i] + y
            ax1.text(x, total + 5, f"{int(total)}", ha="center", va="bottom", fontsize=7, rotation=90)

        # Lower: Line chart (total)
        ax2.plot(df_lower["date"], df_lower["total"], marker="o", label="total", color="cornflowerblue", zorder=2)
        ax2.set_ylabel("stock_volume", color="red", fontsize=12)
        ax2.legend(loc="upper left")
        ax2.grid(True, which="both", axis="y", linestyle="--", zorder=1)

        for x, y in zip(df_lower["date"], df_lower["total"]):
            ax2.text(x, y + 5, f"{int(y)}", ha="center", va="bottom", fontsize=7, rotation=90)

        # Set overall title (optional English only version)
        self.fig.suptitle("Inventory Breakdown: Exceeded vs Within (Upper)\nTotal Stock Volume (Lower)", fontsize=12)

        plt.tight_layout()
        plt.subplots_adjust(top=0.9)

    def save_chart(self, save_dir, chart_type):
        output_path = f"{save_dir}/{chart_type}.png"
        self.fig.tight_layout()
        self.fig.savefig(output_path)
        return output_path
