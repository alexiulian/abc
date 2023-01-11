class validation:
    def __init__(self):
        pass
    def valid(self, adress):
        error = ""
        id = str(adress[0])
        name = adress[1]
        number = adress[2]
        x= str(adress[3])
        y = str(adress[4])

        for i in id:
            if i <= "0" or i >= "9":
                error += "Invalid id!\n"
        for i in name:
            if i <= 'A' or i>= "z":
                error += "Invalid name!\n"
        for i in number:
            if i <= "0" or i >= "9":
                error += "Invalid number!\n"
        for i in x:
            if i != x[0]:
                if i < "0" or i > "9":
                    error += "Invalid x!\n"

        for i in y:
            if i != y[0]:
                if i < "0" or i >"9":
                    error += "Invalid y!\n"

        if (x[0] <= '9' and x[0] >= '0') or x[0] == '-':
            pass
        else:
            error += "Invalid x!\n"

        if (y[0] <= '9' and y[0] >= '0') or y[0] == '-':
            pass
        else:
            error += "Invalid y!\n"

        if len(name) < 3:
            error += "Invalid name!\n"

        if int(x) < -100 or int(x) > 100:
            error += "Invalid x!\n"

        if int(y) < -100 or int(y) > 100:
            error += "Invalid y!\n"

        if int(number) < 0 or int(number) > 100:
            error += "Invalid number!\n"

        if len(error) != 0:
            raise(Exception(error))