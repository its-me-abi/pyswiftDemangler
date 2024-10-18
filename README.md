## pyswiftDemangler
swift programing language symboul demangler / normalizer libarary in  python for windows.
it uses ctypes to normalize symboul by swift official dll binary

>mangling means symbouls are  converted to another form.
so demangling/normalizing is needed to programmatically access it or  understand it visually.
this is needed in reverse engineering executable binary .

## usage

```
import pyswiftdemangler
name = pyswiftdemangler.demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print ( "result = " ,name )
```
