from Repo.Repo import *
from Validator.Validator import *

class service:
    def __init__(self, service_repo, service_validator):
        self.service_repo = service_repo
        self.service_validator = service_validator

    def add_adress(self, adress):
        self.service_validator.valid(adress)
        new_adress = Adress(int(adress[0]), adress[1], int(adress[2]), int(adress[3]), int(adress[4]))
        self.service_repo.add(new_adress)

    def Read_from_file(self):
        return self.service_repo.read_from_file()

    def display_adresses(self):
        return self.service_repo.get_all()