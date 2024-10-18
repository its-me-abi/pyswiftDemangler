## pyswiftDemangler
it returns normalized symboul name if given mangled swift symboul name as input

>mangling means symbouls are  converted to another form.
so demangling/normalizing is needed to programmatically access it or  understand it visually.
this is needed in reverse engineering executable binary .

## usage

```
import pyswiftdemangler
name = pyswiftdemangler.demangler().get_demangled_name("_TtuRxs8RunciblerFxWx5Mince6Quince_")
print ( "result = " ,name )
```
