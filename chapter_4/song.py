class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return "\n".join(self.verse(n) for n in reversed(range(lower, upper + 1)))

    def verse(self, number):
        match number:
            case 0:
                return (
                    # what to do with the "no more" in case 0?
                    "No more bottles of beer on the wall, "
                    f"{self.quantity(number)} bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
            # case 1:
            #     return (
            #         # "case 1 is no longer a special case and can now be handled by the default case"
            #         f"{number} {self.container(number)} of beer on the wall, "
            #         f"{number} {self.container(number)} of beer.\n"
            #         f"Take {self.pronoun(number)} down and pass it around, "
            #         f"{self.quantity(number - 1)} {self.container(number - 1)} of beer on the wall.\n"
            #     )
            case _:
                return (
                    f"{number} {self.container(number)} of beer on the wall, "
                    f"{number} {self.container(number)} of beer.\n"
                    f"Take {self.pronoun(number)} down and pass it around, "
                    f"{self.quantity(number - 1)} {self.container(number - 1)} of beer on the wall.\n"
                )

    def container(self, number: int) -> str:
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def pronoun(self, number: int) -> str:
        if number == 1:
            return "it"
        else:
            return "one"

    def quantity(self, number: int) -> str:
        if number == 0:
            return "no more"
        else:
            return str(number)
