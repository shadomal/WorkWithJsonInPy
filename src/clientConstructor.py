import json
from json import JSONEncoder

class ClienEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Client:
    def __init__(self, user, id, email, address, phone):
        self.user = user
        self.id = id
        self.email = email
        self.address = address
        self.phone = phone

    def create_file():
        with open('client.json', 'w+') as file:
            json.dump({'clients': []}, file)

    def add_client(new_data, fileName='client.json'):
        with open(fileName, 'r+') as file:
            file_data = json.load(file)

            if not file_data.get('clients'):
                file_data = {'clients': list()}

            # use a default dict if json file is empty
            file_data.get('clients').append(
                new_data.toJson() if isinstance(new_data, Client) else new_data
            )

            file.seek(0)
            json.dump(file_data, file)

    def read_client(file_name, key, index, content):
        data = json.load(file_name)
        message = data[key][index][content]
        print(message)

    def toJson(self):
        return self.__dict__
