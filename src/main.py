from clientConstructor import Client

joao = Client("Joao", 1, "joao@gmail.com", "Qr 205 CONJ 07 CASA 02", "9999-9999")

pedro = {
    "user": "pedro",
    "id": 2,
    "email": "pedro_modas@gmail.com",
    "address": "QNL 200 CONJ 10 CASA 30",
    "phone": "8888-8888"
}
julio = {
    "user": "juliao",
    "id": 3,
    "email": "juliao_modas@gmail.com",
    "address": "QNL 230 CONJ 40 CASA 30",
    "phone": "8888-1237"
}

Client.create_file()
Client.add_client(julio)
Client.add_client(pedro)
Client.add_client(joao)
