import os
import csv
import shutil

def isolate_positive_files(csv_file, isolated_folder, positives_subfolder, file_extension=""):
    """
    Reads the CSV file (e.g., GT.csv) and moves files from the isolated_folder
    into a subfolder (positives_subfolder) if the row indicates:
        securecookie,true,614

    Args:
        csv_file (str): Path to the CSV file (e.g., "GT.csv").
        isolated_folder (str): Folder containing all files flagged with vulnerability code "614".
        positives_subfolder (str): Subfolder to hold only the positives (securecookie,true).
        file_extension (str): Optional file extension (e.g., ".java").
    """
    # Create the positives subfolder if it doesn't exist
    if not os.path.exists(positives_subfolder):
        os.makedirs(positives_subfolder)
        print(f"Created subfolder: {positives_subfolder}")

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # Expecting at least 4 columns: filename, tag, flag, vulnerability code
            if len(row) < 4:
                print(f"Skipping malformed row: {row}")
                continue

            filename = row[0].strip()
            tag = row[1].strip()
            flag = row[2].strip().lower()  # normalize to lowercase
            vuln_code = row[3].strip()

            # Check if this row has vulnerability code "614" and securecookie is "true"
            if vuln_code == "614" and tag == "securecookie" and flag == "true":
                # Build the file path in the isolated folder
                source_file = os.path.join(isolated_folder, filename + file_extension)
                if not os.path.exists(source_file):
                    print(f"File not found in isolated folder: {source_file}")
                    continue

                # Build the destination file path within the positives subfolder
                dest_file = os.path.join(positives_subfolder, os.path.basename(source_file))
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(dest_file)
                    count = 1
                    while os.path.exists(f"{base}_{count}{ext}"):
                        count += 1
                    dest_file = f"{base}_{count}{ext}"
                
                try:
                    shutil.move(source_file, dest_file)
                    print(f"Moved positive: {source_file} -> {dest_file}")
                except Exception as e:
                    print(f"Error moving {source_file}: {e}")

if __name__ == "__main__":
    csv_file = "GT.csv"  # CSV file containing your rows
    # The isolated folder (e.g., "Vuln614") contains all files with vulnerability code "614"
    isolated_folder = "Vuln614"
    # The positives subfolder will be created inside the isolated folder
    positives_subfolder = os.path.join(isolated_folder, "positives")
    # Set file_extension if your files have one (for example, ".java")
    file_extension = ".java"  # adjust if needed

    isolate_positive_files(csv_file, isolated_folder, positives_subfolder, file_extension)

