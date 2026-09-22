# Python - Classes & Object Model

This project introduces Object-Oriented Programming in Python: defining
classes, creating instances, managing private attributes with
encapsulation, validating input, and implementing methods and special
methods (`__str__`) to model real-world concepts like `Square` and
`Rectangle`.

## Files

| File | Description |
| --- | --- |
| `0-square.py` | An empty `Square` class with no attributes or methods. |
| `1-square.py` | `Square` with a private `size` attribute set on instantiation. |
| `2-square.py` | `Square` with `size` validated (`TypeError`/`ValueError`) in `__init__`. |
| `3-square.py` | `Square` with an `area()` method. |
| `4-square.py` | `Square` with `size` as a property (getter/setter) with validation. |
| `5-square.py` | `Square` with `my_print()`, printing the square with `#`. |
| `6-square.py` | `Square` with a `position` property and `__str__()`. |
| `1-rectangle.py` | `Rectangle` with private `width`/`height` properties and validation. |
| `2-rectangle.py` | `Rectangle` with `area()` and `perimeter()` methods. |

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
Square = __import__('4-square').Square

my_square = Square(3)
print(my_square.size)
print(my_square.area())
my_square.size = 5
print(my_square.area())
```

Output:

```
3
9
25
```
