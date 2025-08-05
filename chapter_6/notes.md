## Replace conditionals with state/strategy (aka "composition)
- removes conditonals by dispersing their branches into new, smaller objects, one of which is later selected and plugged back in at runtime


## Replace conditionals with polymorphism (aka "inheritance")
- removes conditionals by creating one class to hold the defaults of the conditionals, and adding subclasses for each specialization, then chooses one of the new objects to plug back in at run time

**Polymorphism**:  
> Polymorphism refers to the idea of having many different kinds of objects that
respond to the same message. Senders of the message needn’t
care with which of the possible receivers they are
communicating. Polymorphism allows senders to depend on the
message while remaining ignorant of the type, or class, of the
receiver. Senders don’t care what receivers are; instead, they
depend on what receivers do.

Polymorphism allows you to have different objects that all respond to the same method call, but each can behave differently. 


**Example**:
```python
# Base class with default behavior
class BottleNumber:
    def __init__(self, number):
        self.number = number
    
    def container(self):
        return "bottles"

# Specialized subclasses
class BottleNumberZero(BottleNumber):
    def container(self):
        return "bottles"

class BottleNumberOne(BottleNumber):
    def container(self):
        return "bottle"

class BottleNumberSix(BottleNumber)
    def container(self):
        return "six-pack"

# Usage - polymorphism in action
bottle_zero = BottleNumberZero(0)
bottle_one = BottleNumberOne(1) 
bottle_five = BottleNumber(5)
bottle_six = BottleNumberSix(6)

# The caller doesn't need to know which specific type it is
# It just calls container() and gets the right behavior
for bottle in [bottle_zero, bottle_one, bottle_five, bottle_six]:
    print(bottle.container())  # "bottles", "bottle", "bottles", "six-pack"
```

**The miracle**: You can add new types (like `BottleNumberSix`) without changing any existing code that calls `container()`. The sender remains "ignorant of the type" but still gets the correct behavior.