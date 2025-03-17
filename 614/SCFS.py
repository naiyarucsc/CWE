import os
import csv
import shutil

def move_files_from_csv(csv_file, source_folder, false_dest_folder, true_dest_folder, file_extension=""):
    """
    Reads a CSV file with rows formatted as:
        BenchmarkTest01935,securecookie,false,614
    and moves the corresponding file (from source_folder) to one of two destination folders:
    
    - If the row is "securecookie,false,614", the file is moved to false_dest_folder.
    - If the row is "securecookie,true,614", the file is moved to true_dest_folder.
    
    Args:
        csv_file (str): Path to the CSV file.
        source_folder (str): Folder where the files reside.
        false_dest_folder (str): Destination folder for rows with securecookie,false,614.
        true_dest_folder (str): Destination folder for rows with securecookie,true,614.
        file_extension (str): Optional extension to append to the file name (e.g., ".java").
    """
    
    # Create destination folders if they don't exist
    for folder in (false_dest_folder, true_dest_folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Expecting rows with at least 4 columns: filename, tag, flag, number
            if len(row) < 4:
                print(f"Skipping malformed row: {row}")
                continue
            
            # Strip spaces from each field
            filename = row[0].strip()
            tag = row[1].strip()
            flag = row[2].strip().lower()  # Lowercase flag for consistent checking
            num = row[3].strip()
            
            # Build the source file path
            source_file = os.path.join(source_folder, filename + file_extension)
            
            if not os.path.exists(source_file):
                print(f"Source file not found: {source_file}")
                continue

            # Determine destination based on the CSV row
            if tag == "securecookie" and flag == "false" and num == "614":
                dest_folder = false_dest_folder
            elif tag == "securecookie" and flag == "true" and num == "614":
                dest_folder = true_dest_folder
            else:
                print(f"Row does not match conditions: {row}")
                continue

            # Build the destination file path and avoid overwriting by renaming if necessary
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
    # CSV file containing the lines to inspect
    csv_file = "GT.csv"
    # Source folder where all Java files reside
    source_folder = "testcode"
    # Destination folders for each condition
    false_dest_folder = "FalseFolder"
    true_dest_folder = "TrueFolder"
    
    # IMPORTANT: Set file_extension to ".java" if your files have that extension.
    file_extension = ".java"  # Adjust as needed

    move_files_from_csv(csv_file, source_folder, false_dest_folder, true_dest_folder, file_extension)

