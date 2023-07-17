import os
import shutil
import argparse

def copy_files(source_dir, dest_dir, ignore_patterns):
    ignore_patterns = read_gitignore(source_dir, ignore_patterns)
    files_copied = 0

    # Empty the destination directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        rel_dir = os.path.relpath(root, source_dir)
        dest_subdir = os.path.join(dest_dir, rel_dir)

        # Skip ignored directories
        if any([is_ignored(dir, ignore_patterns) for dir in get_parent_directories(rel_dir)]):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if not is_ignored(file_path, ignore_patterns):
                create_directory(dest_subdir)
                dest_path = os.path.join(dest_subdir, file)
                shutil.copy2(file_path, dest_path)
                files_copied += 1
                print(f"Copied {file_path} to {dest_path}")
                    
    print(f"{files_copied} files have been copied.")

def read_gitignore(source_dir, ignore_patterns):
    ignore_patterns.append('.git')
    gitignore_file = os.path.join(source_dir, '.gitignore')

    if os.path.isfile(gitignore_file):
        with open(gitignore_file, 'r') as f:
            for line in f:
                pattern = line.strip()

                # Skip empty lines or comments in .gitignore
                if pattern and not pattern.startswith('#'):
                    ignore_patterns.append(pattern)

    return ignore_patterns

def is_ignored(path, ignore_patterns):
    rel_path = os.path.relpath(path)

    for pattern in ignore_patterns:
        if pattern.startswith('!'):
            # Negated pattern, check if the path matches
            if matches_pattern(rel_path, pattern[1:]):
                return False
        elif matches_pattern(rel_path, pattern):
            return True

    return False

def matches_pattern(path, pattern):
    if pattern.endswith('/'):
        # Directory pattern
        return path.startswith(pattern.rstrip('/')) and os.path.isdir(path)

    return path == pattern

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_parent_directories(directory):
    directories = []
    parts = directory.split('/')

    for i in range(1, len(parts) + 1):
        parent_dir = '/'.join(parts[:i])
        directories.append(parent_dir)

    return directories

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Python Directory Copy Utility with Exclusion Patterns')
    parser.add_argument('source_dir', help='Path to the source directory')
    parser.add_argument('dest_dir', help='Path to the destination directory')
    parser.add_argument('--exclude', metavar='PATTERN', nargs='+', default=[], help='Exclude patterns')
    args = parser.parse_args()

    # Call the copy_files function with the provided arguments
    copy_files(args.source_dir, args.dest_dir, args.exclude)

if __name__ == '__main__':
    main()