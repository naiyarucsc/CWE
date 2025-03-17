import os
import csv

def load_csv_flags(csv_file):
    """
    Load CSV file into a dictionary mapping filename (without extension) to its securecookie flag.
    Expected CSV format: BenchmarkTest02712,securecookie,false,614
    """
    data = {}
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                continue  # Skip malformed rows
            filename = row[0].strip()  # e.g., BenchmarkTest02712
            flag = row[2].strip().lower()  # "false" or "true"
            data[filename] = flag
    return data

def check_folder_negatives(csv_file, folder, file_extension=""):
    """
    Checks that all files in the folder have a negative flag ("false") as specified in the CSV.
    
    Args:
        csv_file (str): Path to the CSV file (e.g., "GT.csv").
        folder (str): Folder to check (e.g., "V614").
        file_extension (str): The extension of the files (e.g., ".java"). Use "" if none.
    """
    csv_data = load_csv_flags(csv_file)
    all_negative = True
    files_checked = 0

    # List files in the folder that match the extension (if provided)
    for file in os.listdir(folder):
        if file_extension and not file.endswith(file_extension):
            continue
        if not file_extension and os.path.isdir(os.path.join(folder, file)):
            continue  # Skip directories if no extension filtering is done

        files_checked += 1
        # Remove extension for matching the CSV filename
        base_name, _ = os.path.splitext(file)
        if base_name in csv_data:
            flag = csv_data[base_name]
            if flag != "false":
                print(f"File {file} has flag '{flag}', not negative.")
                all_negative = False
        else:
            print(f"File {file} not found in CSV.")
            all_negative = False

    if files_checked == 0:
        print("No files found in the folder.")
    elif all_negative:
        print("All files in the folder are negative.")
    else:
        print("Not all files in the folder are negative.")

if __name__ == "__main__":
    # CSV file containing your rows
    csv_file = "GT.csv"
    # Folder to check (adjust if your folder is named differently, e.g., "Vuln614")
    folder = "Vuln614"
    # Set file_extension to ".java" if your files have that extension; otherwise, set to ""
    file_extension = ".java"  # Adjust or leave as "" if there is no extension

    check_folder_negatives(csv_file, folder, file_extension)

