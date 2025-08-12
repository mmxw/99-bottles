# Chapter 7.2: Fathoming Factories

## Overview: Polymorphism and the Need for Factories

In object-oriented programming, **polymorphism** allows multiple classes to have common APIs, but the implementations of different variants can differ.


### Common API 
All bottle number variants share the same public methods:
- `quantity()` - what to display for quantity
- `container()` - "bottle" vs "bottles" vs special names
- `action()` - what action to take
- `successor()` - what comes next

We want to handle special cases differently:
- **BottleNumber0**: "No more bottles" - different behavior
- **BottleNumber1**: "1 bottle" - singular form
- **BottleNumber6**: "Six-pack" - special marketing case
- **BottleNumberGeneric**: Regular numbers

Each variant would implement the same interface (`quantity()`, `container()`, `action()`, etc.) but with different internal logic.



### Different Implementations
```python
class BottleNumber0:
    def quantity(self):
        return "no more"
    
    def container(self):
        return "bottles"
    
    def action(self):
        return "Go to the store and buy some more"

class BottleNumber1:
    def quantity(self):
        return "1"
    
    def container(self):
        return "bottle"  # Singular!
    
    def action(self):
        return "Take it down and pass it around"

class BottleNumber6:
    def quantity(self):
        return "1"
    
    def container(self):
        return "six-pack"  # Special case!
    
    def action(self):
        return "Take one down and pass it around"
```

### Problem with Direct Object Creation
Without a factory, the `Bottles` class would need to know about all variants:

```python
class Bottles:
    # BAD: Bottles class knows too much
    def verse(self, number):
        if number == 0:
            bottle_number = BottleNumber0()
        elif number == 1:
            bottle_number = BottleNumber1()
        elif number == 6:
            bottle_number = BottleNumber6()
        else:
            bottle_number = BottleNumberGeneric(number)
        # ...
```

**Not so great:**
1. **Tight coupling**: `Bottles` must know all variant classes
2. **Scattered conditionals**: Logic repeated everywhere
3. **Hard to extend**: Adding new variants requires changing `Bottles`

### Factory Pattern Solution

A factory encapsulates the creation logic:

```python
class BottleNumberFactory:
    @staticmethod
    def create(number):
        if number == 0:
            return BottleNumber0()
        elif number == 1:
            return BottleNumber1()
        elif number == 6:
            return BottleNumber6()
        else:
            return BottleNumberGeneric(number)

class Bottles:
    def verse(self, number):
        bottle_number = BottleNumberFactory.create(number)
        next_bottle_number = BottleNumberFactory.create(bottle_number.successor())
        # ...
```

**Benefits:**
1. **Single responsibility**: Factory handles creation, `Bottles` handles song logic
2. **Centralized conditionals**: All creation logic in one place
3. **Loose coupling**: `Bottles` doesn't know variant class names
4. **Easy extension**: Add new variants by modifying only the factory

## Key Principles Demonstrated

### 1. Dependency on Interface, Not Implementation
```python
# Bottles depends on the interface (what), not implementation (how)
bottle_number.quantity()  # Don't care which class, just call quantity()
bottle_number.container() # All variants must respond to container()
bottle_number.action()    # Implementation details hidden
```

### 2. Factories Hide Conditionals
- **Before**: Conditionals scattered throughout code
- **After**: Conditionals isolated in factory
- **Result**: "Conditionals go to die" in factories

