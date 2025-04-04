import os
from config import CHART_CONFIG, chart_dir
from file_manager import move_csv_to_archive

def main():
    """Main function to process CSV files and generate charts."""
    print("🔍 DEBUGGING CONFIGURED PATHS AND FILE EXISTENCE:\n")

    for chart_name, config in CHART_CONFIG.items():
        print(f"🧩 Chart: {chart_name}")
        for file_path in config["files"]:
            exists = os.path.exists(file_path)
            print(f"   └─ 📄 {file_path} → {'✅ Found' if exists else '❌ Missing'}")

    print("\n🚀 Starting chart generation...\n")
    
    for chart_name, config in CHART_CONFIG.items():
        csv_files = [file for file in config["files"] if os.path.exists(file)]
        
        if csv_files:
            chart = config["class"](csv_files)
            print(f"Generating {chart_name}...")

            chart.plot()

            # Save chart in pending directory
            chart.save_chart(chart_dir, chart_type=chart_name)
            # print(f"Saved chart: {saved_chart_path}")

            # Move CSV files to archive
            for csv_file in csv_files:
                pass
                # move_csv_to_archive(csv_file)

        else:
            print(f"No valid files found for {chart_name}")

    # print("📧 Sending charts via email...")
    # subprocess.run(["python", "send_charts.py"])  # Run email script

if __name__ == "__main__":
    main()