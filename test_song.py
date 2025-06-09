from song import Song


def test_generate_verse():
    song = Song()

    assert song.generate_song_verse(0) == (
        "No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
    )

    assert song.generate_song_verse(1) == (
        "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down and pass it around, no more bottles of beer on the wall.\n"
    )

    assert song.generate_song_verse(2) == (
        "2 bottles of beer on the wall, 2 bottles of beer.\n"
        "Take one down and pass it around, 1 bottle of beer on the wall.\n"
    )

    assert song.generate_song_verse(3) == (
        "3 bottles of beer on the wall, 3 bottles of beer.\n"
        "Take one down and pass it around, 2 bottles of beer on the wall.\n"
    )

    assert song.generate_song_verse(99) == (
        "99 bottles of beer on the wall, 99 bottles of beer.\n"
        "Take one down and pass it around, 98 bottles of beer on the wall.\n"
    )


def test_generate_song():
    song = Song()
    assert song.generate_song(0, 10) == (
        "10 bottles of beer on the wall, 10 bottles of beer.\n"
        "Take one down and pass it around, 9 bottles of beer on the wall.\n"
        "\n"
        "9 bottles of beer on the wall, 9 bottles of beer.\n"
        "Take one down and pass it around, 8 bottles of beer on the wall.\n"
        "\n"
        "8 bottles of beer on the wall, 8 bottles of beer.\n"
        "Take one down and pass it around, 7 bottles of beer on the wall.\n"
        "\n"
        "7 bottles of beer on the wall, 7 bottles of beer.\n"
        "Take one down and pass it around, 6 bottles of beer on the wall.\n"
        "\n"
        "6 bottles of beer on the wall, 6 bottles of beer.\n"
        "Take one down and pass it around, 5 bottles of beer on the wall.\n"
        "\n"
        "5 bottles of beer on the wall, 5 bottles of beer.\n"
        "Take one down and pass it around, 4 bottles of beer on the wall.\n"
        "\n"
        "4 bottles of beer on the wall, 4 bottles of beer.\n"
        "Take one down and pass it around, 3 bottles of beer on the wall.\n"
        "\n"
        "3 bottles of beer on the wall, 3 bottles of beer.\n"
        "Take one down and pass it around, 2 bottles of beer on the wall.\n"
        "\n"
        "2 bottles of beer on the wall, 2 bottles of beer.\n"
        "Take one down and pass it around, 1 bottle of beer on the wall.\n"
        "\n"
        "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down and pass it around, no more bottles of beer on the wall.\n"
        "\n"
        "No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
    )
