# Python - Abstract Classes & Interfaces

This project covers abstract base classes (`abc.ABC`, `@abstractmethod`),
duck typing, inheriting from built-in types, multiple inheritance, and
mixins.

## Files

| File | Description |
| --- | --- |
| `animals.py` | Abstract `Animal` class with an abstract `sound()`; `Dog` and `Cat` subclasses implement it. |
| `shapes.py` | Abstract `Shape` interface (`area()`, `perimeter()`); `Circle` and `Rectangle` implement it; `shape_info()` uses duck typing. |
| `flyingfish.py` | `Fish` and `Bird` classes combined via multiple inheritance into `FlyingFish`, which overrides all three shared methods. |
| `dragon.py` | `SwimMixin` and `FlyMixin` combined into `Dragon`, which also adds `roar()`. |
| `verboselist.py` | `VerboseList`, a `list` subclass that announces `append()`, `extend()`, `remove()`, and `pop()`. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8
- Code style checked with `pycodestyle`
- Every file starts with `#!/usr/bin/env python3` and ends with a newline
- Every module, class and method is documented
- No external modules

## Example

`main.py`:

```python
#!/usr/bin/env python3
Animal = __import__('animals').Animal

try:
    Animal()
except TypeError as e:
    print(e)
```

Output:

```
Can't instantiate abstract class Animal with abstract method sound
```
