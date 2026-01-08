# pyswiftdemangler

A **Swift programming language symbol demangler/normalizer library** for Python on Windows.  
It uses Python’s `ctypes` to call the official Swift DLL for demangling Swift mangled symbols.

**Author:** https://github.com/its-me-abi  
**Date:** 18/10/2024

---

## Features

- Demangles Swift symbol names using the official Swift DLL (`swiftDemangle.dll`).
- Exposes a simple Python class interface.
- Provides command-line usage for convenience.
- Offers a test mode to verify correct demangling.

---

## Installation

1. **Requirements:**
   - Python 3.x (Windows)
2. **Setup:**
   - Place `pyswiftdemangler.py` in your project.
   - Ensure `.\lib\swiftDemangle.dll` exists relative to the script, or provide a custom DLL path when initializing.
     usually no need to handle it manuely because it is included in this libarary but if you only copied .py file then make sure dll files are also moved
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
python pyswiftdemangler.py --name <mangled_swift_symbol>
```
**Example:**
```bash
python pyswiftdemangler.py --name _TtuRxs8RunciblerFxWx5Mince6Quince_
```

### Test Mode

To run the built-in test (checks a hardcoded input/output pair):

```bash
python pyswiftdemangler.py --test
```

---

## API Reference

### `demangler` class

- **Constructor:** `demangler(path="")`
  - `path` (optional): Path to the `swiftDemangle.dll`.
  - Defaults to `.\lib\swiftDemangle.dll` relative to the script.

- **Methods:**
  - `get_demangled_name(name, max_buffer_size=0)`
    - Returns the demangled symbol as a string or `None` if demangling fails.
  - *(Internal methods for buffer management and DLL interfacing are also present.)*

---

## File Structure

- `pyswiftdemangler.py` – Main code file.
- `.\lib\swiftDemangle.dll` – Required DLL (not included).

---

## Notes

- Only works in on Windows due to DLL usage.
- Make sure the DLL path is correct; the default expects it in a `lib` folder next to the script.

---

## Example

```python
import pyswiftdemangler

demangler = pyswiftdemangler.demangler()
print(demangler.get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_"))
# Output: <A where A: Swift.Runcible>(A) -> A.Mince.Quince
```
