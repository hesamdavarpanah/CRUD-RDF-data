import os
from pymongo import errors
from ...mongodb_config import MongoDBConfiguration
from datetime import datetime
from socket import gethostbyname, gethostname

class Utility:
    def __init__(self, id, directory_name):
        self.id = id
        self.directory_name = directory_name

    # create directory and file
    def make_directory(self):
        try:
            os.makedirs(f"../{self.directory_name}", exist_ok=True)
            file_save_directory = f"../{self.directory_name}/{self.id}.nt"
            return file_save_directory
        except FileExistsError as error:
            return error
        except NotADirectoryError as error:
            return error

    def file_editor(self):
        try:
            # Remove duplicated data
            uniqlines = set(open(self.make_directory()).readlines())
            open(self.make_directory(), 'w').writelines(uniqlines)

            # Sort characters
            sorted_file = sorted(open(self.make_directory()).readlines())
            open(self.make_directory(), "w").writelines(sorted_file)
        except FileNotFoundError as error:
            return error


class Logger:
    def __init__(self):
        self.mongo_config = MongoDBConfiguration()
        self.client = self.mongo_config.create_client()
        self.database_name = os.getenv("MONGODB_DB_NAME")
        self.collection_name = os.getenv("MONGODB_COLLECTION_NAME")

    def create_database(self):
        try:
            db = self.client[self.database_name]
            return db
        except errors.CollectionInvalid as error:
            return error

    def create_collection(self):
        try:
            collection = self.create_database()[self.collection_name]
            return collection
        except errors.CollectionInvalid as error:
            return error

    def insert_data(self, service_name, message, service_status, data_loaded):
        host_name = gethostname()
        ip_address = gethostbyname(host_name)

        # Create data log
        try:
            data = {
                "service_name": service_name,
                "message": message,
                "log_time": str(datetime.now()),
                "computer_logger_name": host_name,
                "computer_logger_ip": ip_address,
                "service_status": service_status,
                "data_loaded": data_loaded
            }
            self.create_collection().insert_one(data)
        except errors.InvalidDocument as error:
            return error

