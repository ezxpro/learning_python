# Reading and writing files

Here I'm practicing the usage of python's reading and writing capabilities
mainly the `open()` function.

## Documentation
Relevant documentation is for the [open() function](https://docs.python.org/3/library/functions.html#open)

## Important details

- If no locale is specified, `locale.getpreferredencoding(False)` is called when `open`  is called
  - That will get system locale, so locale may change depending on the system if not specified
  - 