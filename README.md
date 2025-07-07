# SplitCSV.py
Takes a CSV file (presumably a large one) and writes 'chunks' of it to separate CSV's at a specified location on the host machine. Each chunk will have the original file's headers and name, with a number added to the end representing what set of rows it has (e.g., 'sample_1.csv' has the first chunk of rows while 'output_8.csv' has the eighth).
## Package Requirements
The script uses the following packages:
```
argparse       # For creating the argument syntax and --help flag
csv            # For writing in CSV
os             # For reading/writing files
sys            # For running the script in the terminal
tqdm           # For displaying a progress bar as the script runs
```
If you don't have any of these packages, you can install them by running the following in your terminal:
```
pip install argparse csv os sys tqdm
```
**Note:** If your system says 'pip' isn't installed or a command, 'pip3' might work instead.
## Running the Script
You can run the script by opening a terminal in its directory (or specifying the filepath to it) and running:
```
python SplitCSV.py {INPUT_FILE_FILEPATH}
```
Where INPUT_FILE_FILEPATH is the file you want to split up.

It can also take several additional arguments in any order after SCANNED_FILEPATH:
```
--help                                                      Shows script syntax without actually running the script (in case this readme isn't up to date).
--output_directory_filepath {OUTPUT_DIRECTORY_FILEPATH}     Filepath for the output directory (default: 'Output')
--chunk_size {CHUNK_SIZE}                                   Integer number of rows each file should have besides the header (default: '24999')
```
These arguments are all optional; any you don't provide will use their specified defaults.

A few extra notes:
- Any files in the output location with the same name as any chunk will likely be overwritten.
- If a directory doesn't exist at the specified output location, one will be made to hold the resulting chunks.
## Generating a Sample CSV
For testing, there is an additional script that can create a CSV to be split up by the original. It uses the same packages and can be run in the same location:
```
python GenerateSampleCSV.py
```
This script does not *require* any arguments, but has several optional, nonpositional ones:
```
--filepath FILEPATH         Filepath and name for resulting CSV file (default: 'sample.csv')
--total_rows TOTAL_ROWS     Integer number of rows resulting file should have besides header (default: 99999)
```
Notes:
- As with the main script, you should specify one *less* than you want for the CSV as the header is techncially a row (e.g., 99999 instead of 100000).
- You can specify a directory to output this file to, and the script will make that directory if it doesn't already exist.
