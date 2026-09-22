# Python – Inheritance & Polymorphism

This project builds a small inheritance hierarchy — `BaseGeometry` ->
`Rectangle` -> `Square` — to practice inheritance, method overriding,
polymorphism, and validation shared across subclasses via
`integer_validator`.

## Files

| File | Description |
| --- | --- |
| `0-polymorphism_demo.py` | `Animal` base class with `Dog`/`Cat` subclasses overriding `speak()`; demonstrates `isinstance()`/`issubclass()`. |
| `base_geometry.py` | `BaseGeometry` with `area()` (raises `Exception`) and `integer_validator()`. |
| `1-rectangle.py` | `Rectangle(BaseGeometry)` with private `width`/`height` validated via `integer_validator`. |
| `2-rectangle.py` | `Rectangle` with `area()` implemented and `__str__()` (`[Rectangle] <width>/<height>`). |
| `1-square.py` | `Square(Rectangle)` initialized from a single `size`. |
| `2-square.py` | `Square` with its own `__str__()` (`[Square] <width>/<height>`). |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8
- Code style checked with `pycodestyle`
- Every file starts with `#!/usr/bin/env python3` and ends with a newline
- Every module, class and method is documented
- No use of `import`/`from` (base classes are loaded with `__import__`)

## Example

`main.py`:

```python
#!/usr/bin/env python3
Square = __import__('2-square').Square

s = Square(5)
print(s)
print(s.area())
```

Output:

```
[Square] 5/5
25
```
