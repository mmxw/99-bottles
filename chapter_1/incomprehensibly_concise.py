class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper_bound: int, lower_bound: int):
        return "\n".join(self.verse(n) for n in range(upper_bound, lower_bound - 1, -1))

    def verse(self, n):
        return (
            f"{'No more' if n == 0 else n} bottle{'s' if n != 1 else ''}"
            f" of beer on the wall, "
            
            f"{'no more' if n == 0 else n} bottle{'s' if n != 1 else ''} of beer.\n"
            + (
                "Go to the store and buy some more, "
                if n == 0
                else f"Take {'one' if n != 1 else 'it'} down and pass it around, "
            )

            + f"{'99' if n - 1 < 0 else ('no more' if n - 1 == 0 else n - 1)} bottle{'s' if n - 1 != 1 else ''}"
            f" of beer on the wall.\n"
        )



































# How difficult was it to write?

# How hard is it to understand?

    # How many verse variants are there?
        # many vs. 3

    # Which verses are most alike? In what way?
    # Which verses are most different, and in what way?
    # What is the rule to determine which verse comes next?

        # Unclear without running the computation in my head


# How expensive will it be to change?

