from .song import Bottles


class TestBottles:
    def setup_method(self):
        self.bottles = Bottles()

    def test_verse_99_bottles(self):
        result = self.bottles.verse(99)
        expected = (
            "99 bottles of beer on the wall, 99 bottles of beer.\n"
            "Take one down and pass it around, 98 bottles of beer on the wall.\n"
        )
        assert result == expected

    def test_verse_2_bottles(self):
        """Test verse for 2 bottles"""
        result = self.bottles.verse(2)
        expected = (
            "2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, 1 bottle of beer on the wall.\n"
        )
        assert result == expected

    def test_verse_1_bottle(self):
        result = self.bottles.verse(1)
        expected = (
            "1 bottle of beer on the wall, 1 bottle of beer.\n"
            "Take it down and pass it around, no more bottles of beer on the wall.\n"
        )
        assert result == expected

    def test_verse_0_bottles(self):
        """Test verse for 0 bottles (special case)"""
        result = self.bottles.verse(0)
        expected = (
            "No more bottles of beer on the wall, no more bottles of beer.\n"
            "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        )
        assert result == expected

    def test_quantity_delegates_to_bottle_number(self):
        """Test that quantity() properly delegates to BottleNumber"""
        assert self.bottles.quantity(5) == "5"
        assert self.bottles.quantity(1) == "1"
        assert self.bottles.quantity(0) == "no more"

    def test_container_delegates_to_bottle_number(self):
        """Test that container() properly delegates to BottleNumber"""
        assert self.bottles.container(5) == "bottles"
        assert self.bottles.container(1) == "bottle"
        assert self.bottles.container(0) == "bottles"

    def test_action_delegates_to_bottle_number(self):
        """Test that action() properly delegates to BottleNumber"""
        assert self.bottles.action(5) == "Take one down and pass it around"
        assert self.bottles.action(1) == "Take it down and pass it around"
        assert self.bottles.action(0) == "Go to the store and buy some more"

    def test_successor_delegates_to_bottle_number(self):
        """Test that successor() properly delegates to BottleNumber"""
        assert self.bottles.successor(5) == 4
        assert self.bottles.successor(1) == 0
        assert self.bottles.successor(0) == 99
