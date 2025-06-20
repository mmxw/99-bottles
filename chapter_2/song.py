class Song:
    def verse(self, number):
        match number:
            case 0:
                return (
                    "No more bottles of beer on the wall, "
                    "no more bottles of beer.\n"
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall.\n"
                )
