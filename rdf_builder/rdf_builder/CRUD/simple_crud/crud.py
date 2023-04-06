from .utility import Utility


class RDFBuilderCRUD:
    def __init__(self, id):
        self.id = id

    def create(self, lang, data, dir_name):
        utility = Utility(id=self.id, directory_name=dir_name)
        # create RDF data from input data
        if not utility.make_directory().__class__ == FileExistsError or utility.__class__ == NotADirectoryError:
            for i in data:
                for key, value in i.items():
                    if value:
                        rdf = f"""<{self.id}> <{key}> "{value}"@{lang} .\n"""
                        file = open(utility.make_directory(), "a+", encoding="utf-8")
                        file.write(rdf)
                        file.close()
            utility.file_editor()
            return "RDF data created"
        else:
            return utility.make_directory().__str__()

