import os


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """

    directories_seen, files_seen = 0, 0

    for root, subdirs, files in os.walk(directory):
        directories_seen += len(subdirs)
        files_seen += len(files)

    return (directories_seen, files_seen)


if __name__ == "__main__":
    print(count_dirs_and_files())
