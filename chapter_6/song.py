class Bottles:
    # ...
    def verse(self, number):
        bottle_number = BottleNumber(number)
        next_bottle_number = BottleNumber(bottle_number.successor())

        return (
            f"{bottle_number} of beer on the wall, ".capitalize() +
            f"{bottle_number} of beer.\n"
            f"{bottle_number.action()}, "
            f"{next_bottle_number}"
            " of beer on the wall.\n"
        )
    def quantity(self, number):
        # return BottleNumber(number).quantity(number)
        return BottleNumber(number).quantity()

    def container(self, number):
        return BottleNumber(number).container()

    def action(self, number):
        return BottleNumber(number).action()

    def successor(self, number):
        return BottleNumber(number).successor()
    def quantity(self, number):
        return BottleNumber(number).quantity()

    def container(self, number):
        return BottleNumber(number).container()

    def action(self, number):
        return BottleNumber(number).action()

    def successor(self, number):
        return BottleNumber(number).successor()


class BottleNumber:
    def __init__(self, number):
        self._number = number

    def __str__(self):
        return f"{self.quantity()} {self.container()}"

    def quantity(self):
        if self._number == 0:
            return "no more"
        return str(self._number)

    def container(self):
        if self._number == 1:
            return "bottle"
        return "bottles"

    def action(self):
        if self._number == 0:
            return "Go to the store and buy some more"
        return f"Take {self.pronoun()} down and pass it around"

    def pronoun(self):
        if self._number == 1:
            return "it"
        return "one"

    def successor(self):
        if self._number == 0:
            return 99
        return self._number - 1
