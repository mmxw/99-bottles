class Song:
    def generate_song_verse(self, number: int) -> str:
        match number:
            case 0:
                return (
                    "No more bottles of beer on the wall, no more bottles of beer.\n"
                    "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
                )
            case 1:
                return (
                    "1 bottle of beer on the wall, 1 bottle of beer.\n"
                    "Take it down and pass it around, no more bottles of beer on the wall.\n"
                )
            case 2:
                return (
                    "2 bottles of beer on the wall, 2 bottles of beer.\n"
                    "Take one down and pass it around, 1 bottle of beer on the wall.\n"
                )
            case _:
                return (
                    f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
                    f"Take one down and pass it around, {number - 1} bottles of beer on the wall.\n"
                )

    def generate_song(self, lower_bound: int, upper_bound: int) -> str:
        song = []
        for number in range(upper_bound, lower_bound - 1, -1):
            song.append(self.generate_song_verse(number))
        return "\n".join(song)


song = Song().generate_song(0, 99)
print(song)
