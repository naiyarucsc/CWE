import os
import csv
import shutil

def move_vulnerable_files(csv_file, source_folder, dest_folder, file_extension=""):
    """
    Reads a CSV file (GT.csv) where each row is formatted as:
        BenchmarkTest01935,securecookie,false,614
    and moves files from the source folder (JTCs/testcode) to the destination folder
    if the vulnerability code (fourth column) is "614".

    Args:
        csv_file (str): Path to the CSV file (e.g., "GT.csv").
        source_folder (str): Folder where the files reside (e.g., "JTCs/testcode").
        dest_folder (str): Folder where vulnerable files will be moved.
        file_extension (str): Optional extension to append to the file name (e.g., ".java").
    """
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created folder: {dest_folder}")

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                print(f"Skipping malformed row: {row}")
                continue

            filename = row[0].strip()
            vuln_code = row[3].strip()  # Vulnerability code is in the fourth column

            # Only process rows with vulnerability code "614"
            if vuln_code != "614":
                continue

            # Build the source file path (adding file_extension if necessary)
            source_file = os.path.join(source_folder, filename + file_extension)
            if not os.path.exists(source_file):
                print(f"Source file not found: {source_file}")
                continue

            # Build the destination file path, avoiding overwrites if needed
            dest_file = os.path.join(dest_folder, os.path.basename(source_file))
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(dest_file)
                count = 1
                while os.path.exists(f"{base}_{count}{ext}"):
                    count += 1
                dest_file = f"{base}_{count}{ext}"

            try:
                shutil.move(source_file, dest_file)
                print(f"Moved: {source_file} -> {dest_file}")
            except Exception as e:
                print(f"Error moving {source_file}: {e}")

if __name__ == "__main__":
    # Path to your CSV file
    csv_file = "GT.csv"
    # Folder where your Java files reside
    source_folder = "testcode"
    # Destination folder for files that have vulnerability code "614"
    dest_folder = "Vuln614"
    # If your files have an extension, such as ".java", set it below
    file_extension = ".java"  # or "" if there's no extension

    move_vulnerable_files(csv_file, source_folder, dest_folder, file_extension)

