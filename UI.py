from Service.Service import *
from Domain.Domain import *

class ui:
    def __init__(self, ui_service):
        self.ui_service = ui_service
        self.next_id = 11
        self.commands = {
            '1': self.__ui__add_adress,
            '2': self.__ui__display_adress,
            '3':10
        }

    def read_file(self):
        self.ui_service.Read_from_file()

    def __ui__add_adress(self):
        print("Your adresss should look like: <any_id>,<name>,<number>,<x>,<y>")
        print("Id will be set automatically.")
        adress = input("Your adress: ")
        adress = adress.split(",")
        adress[0] = self.next_id
        self.next_id += 1
        self.ui_service.add_adress(adress)

    def __ui__display_adress(self):
        for i in self.ui_service.display_adresses():
            adress = self.ui_service.display_adresses()[i]
            print(adress)

    def run(self):
        print()
        print()
        print()
        print()
        self.read_file()
        while True:

            command = input("Your command: ")

            if command == "":
                continue
            elif command == "0":
                break
            elif command in self.commands:

                try:

                    self.commands[command]()

                except ValueError:
                    print("UI error, invalid input!")
                except validation as ve:
                    print(f"Validation error {ve}")
                except repo as re:
                 print(f"Repo error {re}")
