from Domain.Domain import *
from Repo.Repo import *
from Service.Service import *
from Validator.Validator import *
from UI.UI import *

if __name__ == "__main__":
    repo_of_adress = repo()
    validator_of_adress = validation()
    service_of_addres = service(repo_of_adress, validator_of_adress)

    ui_of_adress = ui(service_of_addres)
    ui_of_adress.run()