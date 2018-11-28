class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]

    def __repr__(self):
        str_to_return = ""
        power_counter = self.coefficients.__len__() - 1
        for coefficient in self.coefficients[::-1]:
            if coefficient == 0:
                pass
            elif power_counter == 0:
                str_to_return += str(coefficient) + " "
            elif power_counter == 1:
                if coefficient == 1:
                    str_to_return += "x + "
                else:
                    str_to_return += str(coefficient) + "x" + " + "
            elif coefficient == 1:
                str_to_return += "x^" + str(power_counter) + " + "
            else:
                str_to_return += str(coefficient) + "x^" + str(power_counter) + " + "
            power_counter -= 1
        return str_to_return

