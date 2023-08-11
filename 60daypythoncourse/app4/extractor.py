import zipfile

def extract_archive(archive_path, destination_directory):
    with zipfile.ZipFile(archive_path, 'r') as ar:
        ar.extractall(destination_directory)

