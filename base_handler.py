from abc import ABC, abstractmethod
import pandas as pd
import os

class BaseChart(ABC):
    """Abstract base class for generating charts from one or multiple CSV files."""

    def __init__(self, file_paths):
        """
        file_paths: List of CSV file paths (one or multiple).
        output_dir: Directory to save the chart images.
        """
        self.file_paths = file_paths
        self.dataframes = self.load_data()

        # Ensure output directory exists
        # os.makedirs(self.output_dir, exist_ok=True)

    def load_data(self):
        """Load all CSV files into a dictionary of pandas DataFrames."""
        data_dict = {}
        for file_path in self.file_paths:
            file_name = os.path.basename(file_path)  # Extract filename for identification
            try:
                df = pd.read_csv(file_path)
                if df.empty:
                    print(f"Warning: {file_name} is empty.")
                data_dict[file_name] = df
            except Exception as e:
                print(f"Error loading file {file_name}: {e}")
        return data_dict

    @abstractmethod
    def plot(self):
        """Abstract method to plot the chart."""
        pass

    @abstractmethod
    def save_chart(self, save_dir, chart_type):
        """Abstract method to save the chart to a file."""
        pass

