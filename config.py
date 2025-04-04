import os
from chart_handler import Chart611
from chart_handler import Chart622
from chart_handler import Chart615
from chart_handler import Chart616

script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths for data and chart directories
data_dir = os.path.join(script_dir, r'data\pending')
data_archive_dir = os.path.join(script_dir, r'data\archive')
chart_dir = os.path.join(script_dir, r'chart\pending')
chart_archive_dir = os.path.join(script_dir, r'chart\archive')

# Define chart configurations
CHART_CONFIG = {
    "chart611": {
        "class": Chart611,
        "files": ["611_upper.csv", "611_lower.csv"]  # Multiple CSVs supported
    },
    "chart622": {
        "class":Chart622,
        "files": ["622_upper.csv", "622_lower.csv"]
    },
    "chart615": {  
        "class": Chart615,
        "files": ["615_upper.csv", "615_lower.csv"]
    },
    "chart616": {
        "class": Chart616,
        "files": ["616_0.csv", "616_1.csv", "616_2.csv", "616_3.csv", "616_4.csv"]
    }
}

# Convert relative paths to absolute paths
for chart in CHART_CONFIG.values():
    chart["files"] = [os.path.join(data_dir, file) for file in chart["files"]]
