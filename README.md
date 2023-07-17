# Python Directory Copy Utility with Exclusion Patterns

This is a Python command-line utility that allows you to copy directories while excluding certain files or folders based on patterns defined in a .gitignore file.

## Features

- Copy directories while excluding files/folders based on patterns
- Supports reading exclusion patterns from .gitignore files
- Maintains the original file structure during the copying process

## Usage

1. Clone or download this repository to your local machine.

2. Run the script with the following command:

```shell
python copy_files.py [source_directory] [destination_directory] --exclude [pattern1] [pattern2] ...
```

 * Replace **'[source_directory]'** with the path to the source    directory you want to copy.
 * Replace **'[destination_directory]'** with the path to the destination directory where the files will be copied.
 * Optionally, specify one or more exclusion patterns with the **'--exclude'** option. These patterns should follow the syntax of .gitignore file patterns.

3. The script will copy the files from the source directory to the destination directory, excluding any files or folders that match the specified exclusion patterns.

## Examples
Copy files from the source directory **'/path/to/source'** to the destination directory **'/path/to/destination'**, excluding all files with the **'.txt'** extension:

```shell
python copy_files.py /path/to/source /path/to/destination --exclude "*.txt"
```
## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.