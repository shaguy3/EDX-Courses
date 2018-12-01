class Polynomial:

    def __init__(self, *coefficients):
        """Creates a new polynomial given a list of coefficients in decreasing order(highest power to lowest power)"""
        self.coefficients = coefficients[::-1]

    def __repr__(self):
        """Returns a string representation of the polynomial"""
        representation = ""
        power_counter = self.coefficients.__len__() - 1
        for coefficient in self.coefficients[::-1]:
            if coefficient == 0:
                pass
            elif coefficient == 1:
                if power_counter == 0:
                    representation += "+"
                elif power_counter == 1:
                    representation += "+x"
                else:
                    representation += "+x^" + str(power_counter)
            elif coefficient == -1:
                if power_counter == 0:
                    representation += "-1"
                elif power_counter == 1:
                    representation += "-x"
                else:
                    representation += "-x^" + str(power_counter)
            elif coefficient > 0:
                if power_counter == 0:
                    representation += "+" + str(coefficient)
                elif power_counter == 1:
                    representation += "+" + str(coefficient) + "x"
                else:
                    representation += "+" + str(coefficient) + "x^" + str(power_counter)
            else:
                if power_counter == 0:
                    representation += "-" + str(abs(coefficient))
                elif power_counter == 1:
                    representation += "-" + str(abs(coefficient)) + "x"
                else:
                    representation += "-" + str(abs(coefficient)) + "x^" + str(power_counter)
            power_counter -= 1
        if self.coefficients[0] >= 0:
            representation = representation[1:]
        return representation

    def __call__(self, x):
        """Returns the result of the function given a certain x value"""
        res = 0
        for index, coefficient in enumerate(self.coefficients):
            res += coefficient * x ** index
        return res

    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1

    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)


p1 = Polynomial(-1, 2, -1)
print(p1)
p2 = Polynomial(-6, 4)
print(p2)
