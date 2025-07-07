import argparse         # https://docs.python.org/3/library/argparse.html   # License: Python Software Foundation (Version 2)
import csv              # https://docs.python.org/3/library/csv.html        # License: Python Software Foundation (Version 2)
import os               # https://docs.python.org/3/library/os.html         # License: Python Software Foundation (Version 2)
import sys              # https://docs.python.org/3/library/sys.html        # License: Python Software Foundation (Version 2)
from tqdm import tqdm   # https://github.com/tqdm/tqdm                      # License: MIT


def SplitCSV(input_file, output_directory="Output", chunk_name="csv_chunk", chunk_size=24999):
    os.makedirs(output_directory, exist_ok=True)                                            # Make output directory if it doesn't exist.
    base_name = os.path.splitext(os.path.basename(input_file))[0]                           # Get the name of the file being split up.

    with open(input_file, mode='r', encoding='utf-8-sig') as f:
        total_rows = sum(1 for _ in f) - 1                                                  # Count total rows (excluding header) for progress bar

    with open(input_file, mode='r', newline='', encoding='utf-8-sig') as infile:            # Use utf-8-sig as some encodings have hidden characters.
        reader = csv.reader(infile)
        header = next(reader)                                                               # Get next row in CSV.

        file_count = 1
        rows = []
        row_iter = tqdm(reader, total=total_rows, desc="Splitting CSV")                     # Show progress of splitting file.

        for i, row in enumerate(row_iter, 1):                                               # For each row in the file:
            rows.append(row)                                                                # Append row to list of rows to write to next chunk.
            if i % chunk_size == 0:                                                         # If more than a chunk's worth of rows left:
                out_path = os.path.join(output_directory, f"{base_name}_{file_count}.csv")  # Get filepath to write the current chunk.
                with open(out_path, mode='w', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(header)                                                 # Write header.
                    writer.writerows(rows)                                                  # Write rows.
                file_count += 1
                rows = []                                                                   # Clear list for next chunk (if any).

        if rows:                                                                            # If there are rows left that fit in a single chunk:
            out_path = os.path.join(output_directory, f"{base_name}_{file_count}.csv")      # Prepare last chunk.
            with open(out_path, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)                                                     # Write header.
                writer.writerows(rows)                                                      # Write rows.

# Running the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Takes a CSV file and splits it into smaller files with no more than 24,999 rows (and header).")
    parser.add_argument("input_file_filepath", help="Filepath to the CSV to be split")
    parser.add_argument("--output_directory_filepath", default="Output", help="Filepath for the output directory (default: 'Output')")
    parser.add_argument("--chunk_size", default=24999, help="Integer number of rows each file should have besides the header (default: '24999')")


    args = parser.parse_args()
    try:
        SplitCSV(args.input_file_filepath, args.output_directory_filepath, args.chunk_size)
    except KeyboardInterrupt: # Usually Ctrl+C
        print("\nScan stopped by user. Exiting script.")
        sys.exit(0)