## 4.3 Deriving names from responsibilities

- Responsibility : a name's responsibility is to represent the concept as understood
    - `pronoun`: `it` or `one`

- Question: how to choose a name to represent a concept that's less clear-cut?
    ```python
        case 1:
            return (
                ...
                "no more bottles of beer on the wall.\n"
            )
        case _:
            return (
                ...
                f"{number - 1} {self.container(number - 1)} of beer on the wall.\n"
            )
    ```
    - differences and conditions for the differences
        [placeholder]    [container]   [number]
        "no more"          bottles        0
        "1"                bottle         1
        "2"                bottles        2
        "99"               bottles        99
        
## 4.4 Choosing meaningful Default
    - option 1: `remainder`
        [remainder]    [container]   [number]
        "no more"          bottles        0
        "1"                bottle         1
        "2"                bottles        2
        "99"               bottles        99