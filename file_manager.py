import os
import shutil
import datetime
from config import data_archive_dir

def move_csv_to_archive(csv_file_path):
    """Move a CSV file to the archive directory with a timestamped filename.

    Args:
        csv_file_path (str): Path to the CSV file to be moved.
    """
    if not os.path.exists(csv_file_path):
        print(f"❌ File not found: {csv_file_path}")
        return None

    # Extract original filename and add timestamp
    base_name = os.path.basename(csv_file_path)
    file_name, file_ext = os.path.splitext(base_name)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    new_file_name = f"{file_name}_{timestamp}{file_ext}"
    new_file_path = os.path.join(data_archive_dir, new_file_name)

    # Move the file
    try:
        shutil.move(csv_file_path, new_file_path)
        print(f"✅ Moved CSV to archive: {new_file_path}")
        return new_file_path
    except Exception as e:
        print(f"❌ Error moving CSV file: {e}")
        return None
