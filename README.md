# pyswiftdemangler

A **Swift programming language symbol demangler/normalizer library** for Python on Windows (unofficial).  
It uses Python's `ctypes` to call the official Swift DLL for demangling Swift mangled symbols.

**Author:** https://github.com/its-me-abi  
**Date:** 18/10/2024

---

## Features

- Demangles Swift symbol names using the official Swift DLL (`swiftDemangle.dll`).
- Exposes a simple Python class interface.
- Provides command-line usage for convenience.
- Offers a test mode to verify correct demangling.
- Installable as a PyPI package.

---

## Installation

### From PyPI (recommended)

```bash
pip install pyswiftdemangler
```

### From source

```bash
git clone https://github.com/its-me-abi/pyswiftDemangler.git
cd pyswiftDemangler
pip install -e .
```

### Requirements

- Python 3.6 or higher
- Windows OS (due to DLL usage)
- `swiftDemangle.dll` (included in the package, or provide a custom path)

---

## Usage

### As a Library

```python
from pyswiftdemangler import demangler

d = demangler()  # or demangler(path_to_dll)
demangled = d.get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print(demangled)  # Outputs: <A where A: Swift.Runcible>(A) -> A.Mince.Quince
```

### From the Command Line

```bash
pyswiftdemangler --name <mangled_swift_symbol>
```

**Example:**
```bash
pyswiftdemangler --name _TtuRxs8RunciblerFxWx5Mince6Quince_
```

### Test Mode

To run the built-in test (checks a hardcoded input/output pair):

```bash
pyswiftdemangler --test
```

---

## API Reference

### `demangler` class

```python
from pyswiftdemangler import demangler

d = demangler(path="")
```

**Parameters:**
- `path` (str, optional): Path to the `swiftDemangle.dll`. Defaults to the bundled DLL.

**Methods:**
- `get_demangled_name(name, max_buffer_size=0)`
  - Returns the demangled symbol as a string or `None` if demangling fails.
  - `name` (str): The mangled Swift symbol name.
  - `max_buffer_size` (int): Optional maximum buffer size for output.

**Example:**
```python
from pyswiftdemangler import demangler

demangler_instance = demangler()
demangled = demangler_instance.get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print(demangled)  # <A where A: Swift.Runcible>(A) -> A.Mince.Quince
```

---

## File Structure

```
pyswiftDemangler/
├── pyswiftdemangler/
│   ├── __init__.py          # Package initialization
│   ├── core.py              # Main demangler implementation
│   ├── cli.py               # Command-line interface
│   └── lib/
│       └── swiftDemangle.dll # Swift DLL (required for demangling)
├── README.md                # This file
├── LICENSE                  # MIT License
├── CHANGELOG.md             # Version history
├── pyproject.toml           # Modern Python packaging config
├── setup.py                 # Legacy setup script
├── setup.cfg                # Setup configuration
└── MANIFEST.in              # Package manifest
```

---

## Notes

- Only works on Windows due to DLL usage.
- Ensure the DLL path is correct; the default expects it in the `lib` folder within the package.
- If you get a DLL loading error, verify that `swiftDemangle.dll` exists in the package `lib` directory.

---

## Example

```python
import pyswiftdemangler

demangler = pyswiftdemangler.demangler()
print(demangler.get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_"))
# Output: <A where A: Swift.Runcible>(A) -> A.Mince.Quince
```

---

## Development

### Running Tests

```bash
pyswiftdemangler --test
```

### Building the Package

```bash
pip install build
python -m build
```

This creates `dist/` directory with wheel (`.whl`) and source (`.tar.gz`) distributions.

### Publishing to PyPI

```bash
pip install twine
twine upload dist/*
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
