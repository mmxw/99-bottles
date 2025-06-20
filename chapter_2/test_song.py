from song import Song


def test_verse_0():
    song = Song()
    expected = (
        "No more bottles of beer on the wall, "
        "no more bottles of beer.\n"
        "Go to the store and buy some more, "
        "99 bottles of beer on the wall.\n"
    )
    assert song.verse(0) == expected


def test_verse_1():
    song = Song()
    expected = (
        "1 bottle of beer on the wall, "
        "1 bottle of beer.\n"
        "Take it down and pass it around, "
        "no more bottles of beer on the wall.\n"
    )
    assert song.verse(1) == expected
