## pyswiftDemangler
swift programing language symbol demangler / normalizer libarary in  python for windows.
it uses ctypes to normalize symbol by swift official dll binary

>Mangling means the process where symbols (such as function names or variables) are converted into a different form,  Demangling, or normalizing, is necessary to programmatically access these symbols or understand them visually. This process is crucial in reverse engineering executable binaries.

I was inspired by lauri kirk 's swiftdemangler
## usage

```
import pyswiftdemangler
name = pyswiftdemangler.demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print ( name )
```
