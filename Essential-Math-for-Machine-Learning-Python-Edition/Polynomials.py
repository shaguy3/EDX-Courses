class Polynomial:

    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]

    def __repr__(self):
        representation = ""
        power_counter = self.coefficients.__len__() - 1
        for coefficient in self.coefficients[::-1]:
            if coefficient == 0:
                pass
            elif coefficient > 0:
                if power_counter == 0:
                    representation += " + " + str(coefficient)
                elif power_counter == 1:
                    representation += " + " + str(coefficient) + "x"
                else:
                    representation += " + " + str(coefficient) + "x^" + str(power_counter)
            else:
                if power_counter == 0:
                    representation += " - " + str(abs(coefficient))
                elif power_counter == 1:
                    representation += " - " + str(abs(coefficient)) + "x"
                else:
                    representation += " - " + str(abs(coefficient)) + "x^" + str(power_counter)
            power_counter -= 1
        representation = representation[3:]
        return representation


print(Polynomial(2, -5, 0, 3).__repr__())
