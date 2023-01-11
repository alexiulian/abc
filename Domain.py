class Adress:

    def __init__(self, id, name, number , x, y):

        self.id = id
        self.name= name
        self.number= number
        self.x= x
        self.y = y

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_number(self):
        return self.number

    def set_number(self, new_number):
        self.number = new_number

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return "Id: " + str(self.id) + ", Name: " + self.name + ", Number: " + str(self.number) + ", Y: " + str(self.y) + ", X: " + str(self.y)