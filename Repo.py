from Domain.Domain import *
import copy

class repo:
    def __init__(self):
        self.list_of_adress = {}
    def add(self, adress: Adress):
        self.list_of_adress[adress.get_id()] = adress

    def get_all(self):
        return self.list_of_adress

    def read_from_file(self):
        file_name = "D:\\Probleme_FP\\PB_02\\file.txt"

        lines = []

        try:
            fin = open(file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError:
            pass
        print(lines)
        for line in lines:
            line = line.split(",")
            #print(line)
            last_one = line[4]
            if last_one[-1] == "\n":
                last_one = last_one[:-1]
                line[4] = last_one
            #print(line[4])
            new_adress = Adress(int(line[0]), line[1], int(line[2]), int(line[3]), int(line[4]))
            self.add(new_adress)


