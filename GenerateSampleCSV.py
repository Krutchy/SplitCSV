import argparse         # https://docs.python.org/3/library/argparse.html   # License: Python Software Foundation (Version 2)
import csv              # https://docs.python.org/3/library/csv.html        # License: Python Software Foundation (Version 2)
import os               # https://docs.python.org/3/library/os.html         # License: Python Software Foundation (Version 2)
import sys              # https://docs.python.org/3/library/sys.html        # License: Python Software Foundation (Version 2)
from tqdm import tqdm   # https://github.com/tqdm/tqdm                      # License: MIT

def GenerateSampleCSV(filepath='Samples/sample.csv', total_rows=99999):
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    header = ['ID', 'Name', 'Value']
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in tqdm(range(1, total_rows + 1), desc="Generating CSV"):
            writer.writerow([i, f'Name_{i}', f'Value_{i}'])

# Running the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Takes a CSV file and splits it into smaller files with no more than 24,999 rows (and header).")
    parser.add_argument("--filepath", default="Samples/sample.csv", help="Filepath and name for resulting CSV file (default: 'sample.csv')")
    parser.add_argument("--total_rows", default=99999, help="Integer number of rows resulting file should have besides header (default: 99999)")


    args = parser.parse_args()
    try:
        GenerateSampleCSV(args.filepath, args.total_rows)
    except KeyboardInterrupt: # Usually Ctrl+C
        print("\nScan stopped by user. Exiting script.")
        sys.exit(0)
