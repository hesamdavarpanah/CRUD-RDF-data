# Extract ID, language and remained data from json input
class DataReader:
    def __init__(self, input):
        self.input = input
        self.extrac_data = []

    # Extract ID
    @property
    def get_id(self):
        return self.input["id"]

    # Extract language
    @property
    def get_language(self):
        for i in self.input["main_fields"]:
            return i["lang"]

    # Extract data
    @property
    def get_data(self):
        for i in self.input["main_fields"]:
            for aliases in i["aliases"]:
                self.extrac_data.append({"aliases": aliases})
            i.pop("lang") and i.pop("aliases")
            for key, value in i.items():
                self.extrac_data.append({key: value})
            return self.extrac_data
