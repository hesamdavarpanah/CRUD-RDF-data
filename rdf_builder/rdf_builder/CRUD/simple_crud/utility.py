import os


class Utility:
    def __init__(self, id, directory_name):
        self.id = id
        self.directory_name = directory_name

    # create directory and file
    def make_directory(self):
        os.makedirs(f"../{self.directory_name}", exist_ok=True)
        file_save_directory = f"../{self.directory_name}/{self.id}.nt"
        return file_save_directory

    def file_editor(self):
        # Lowercase all characters
        file = open(self.make_directory(), "r")
        lines = [line.lower() for line in file]
        with open(self.make_directory(), "w+") as out:
            out.writelines(sorted(lines))

        # Remove duplicated data
        uniqlines = set(open(self.make_directory()).readlines())
        bar = open(self.make_directory(), 'w').writelines(uniqlines)

        # Sort characters
        sorted_file = sorted(open(self.make_directory()).readlines())
        sort_line = open(self.make_directory(), "w").writelines(sorted_file)
