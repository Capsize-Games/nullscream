# NULLSCREAM

---

![img.png](img.png)

---

`nullscream` is a simple library that allows you to
import noop functions and classes that you can use as drop in replacements for functions you wish to override.

This allows anything on the blacklist to be importable, but not executable.

## Installation

```bash
pip install nullscream
```

## Usage

Import the `install_nullscream` function the top of your main entry file (e.g. `main.py`), import `nullscream` before 
importing any other libraries.

```python
from nullscream import install_nullscream
```

Specify what you would like to blacklist

```python
install_nullscream(
    blacklist=[
        "requests"
    ]
)
```

Now when you import requests, you will get a noop version of the requests library.

```python
import requests

print(requests.__doc__)

# Output:
# This is a noop stand-in module.

print(requests.foobar())

# Output:
# MagicType instance
```

You can uninstall the noop module by calling `uninstall_nullscream`

```python
from nullscream import uninstall_nullscream
uninstall_nullscream(
    blacklist=["requests"]
)
```

Now when you import requests, you will get the original requests library.

```python
import requests

print(requests.__doc__)

# Output: Original requests library docstring
```

---

## Testing

```bash
python -m unittest discover -s tests
```
