# Python - Exception Handling

This project covers how to handle and raise exceptions in Python with
`try`, `except`, `finally` and `raise`.

## Files

| File | Description |
| --- | --- |
| `safe_print_list.py` | Prints the first `x` elements of a list on one line and returns the number of elements printed. |
| `safe_print_integer.py` | Prints a value with `"{:d}".format()` and returns `True` if it is an integer, `False` otherwise. |
| `safe_print_list_integers.py` | Prints only the integers found in the first `x` elements of a list and returns how many were printed. |
| `safe_print_division.py` | Divides two numbers, always prints `Inside result: <result>` using `finally`, and returns the result (or `None`). |
| `raise_exception.py` | Raises a `TypeError`. |
| `raise_exception_msg.py` | Raises a `NameError` with a custom message. |

## Requirements

- Python 3
- Code style checked with `pycodestyle`
- No module imports in these files

## Example

`main.py`:

```python
#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

nb_print = safe_print_list([1, 2, 3, 4, 5], 2)
print("nb_print: {:d}".format(nb_print))
```

Output:

```
12
nb_print: 2
```
