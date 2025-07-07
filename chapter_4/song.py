class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return "\n".join(self.verse(n) for n in reversed(range(lower, upper + 1)))

    def verse(self, number):
        match number:
            case 0:
                return (
                    "No more bottles of beer on the wall, "
                    "no more bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
            case 1:
                return (
                    f"{number} {self.container(number)} of beer on the wall, "
                    f"{number} {self.container(number)} of beer.\n"
                    f"Take {self.pronoun(number)} down and pass it around, "
                    "no more bottles of beer on the wall.\n"
                )
            case _:
                return (
                    f"{number} {self.container(number)} of beer on the wall, "
                    f"{number} {self.container(number)} of beer.\n"
                    f"Take {self.pronoun(number)} down and pass it around, "
                    f"{number - 1} {self.container(number - 1)} of beer on the wall.\n"
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
