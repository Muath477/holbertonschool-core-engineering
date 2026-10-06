# Python – File Handling

This project covers Python's file input/output: opening files, writing,
appending, reading the full content, and making sure resources are released
with the `with` statement.

## Files

| File | Description |
| --- | --- |
| `read_file.py` | `read_file(filename="")` reads a UTF-8 text file and prints its content to stdout. |
| `write_file.py` | `write_file(filename="", text="")` overwrites (or creates) a UTF-8 text file and returns the number of characters written. |
| `append_write.py` | `append_write(filename="", text="")` appends a string to a UTF-8 text file (or creates it) and returns the number of characters added. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code style checked with `pycodestyle` (2.7.*)
- Every file starts with `#!/usr/bin/env python3` and ends with a newline
- Every module and function is documented
- Files are opened with the `with` statement
- No file permission or missing-file exception handling is required
- No modules are imported

## Example

`1-main.py`:

```python
#!/usr/bin/env python3
write_file = __import__('write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
```

Output:

```
24
```
