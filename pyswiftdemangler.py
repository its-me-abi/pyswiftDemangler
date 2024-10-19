import ctypes,os,argparse,sys

"""
swift programing language symbol demangler / normalizer libarary in  python for windows
it uses ctypes to normalize symbol by swift official dll binary
author : abilash 18/10/2024
"""

MAX_SYMBOL_LENGTH = 4096 # maximum buffer size for ctypes array.

class demangler:
    libname = r".\lib\swiftDemangle.dll"
    default_path = os.path.normpath(os.path.join(os.path.dirname(__file__), libname))

    def __init__(self , path = ""):
        self.dll_path = path or self.default_path
        self.libswift = ctypes.WinDLL( self.dll_path )
        self.demangle = self.libswift.fnd_get_demangled_name
        self.demangle.restype = ctypes.c_int
        self.demangle.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

    def get_buffersize(self,max_buffer_size):
        return max_buffer_size or MAX_SYMBOL_LENGTH

    def crete_input_array(self,name):
        "returns ctypes buffer for both input "
        char_array = ( ctypes.c_char * ( len(name)+1 ))()
        ctypes.memmove ( char_array , name, len(name) )
        return char_array

    def crete_output_array(self,buffer_size):
        "returns ctypes buffer for both input and output"
        char_array = ( ctypes.c_char * ( buffer_size ))()
        return char_array

    def get_demangled_name(self, name, max_buffer_size = 0):
        result_length,val = self._normalize(name,max_buffer_size )
        if result_length  :
            target_output_buffer_lenth = self.get_buffersize(max_buffer_size)
            if result_length > target_output_buffer_lenth:
                "if result is greater than buffer then rerun the process with target buffer size"
                result_length, val = self._normalize(name,max_buffer_size = result_length+1)
            return val.decode()

    def _normalize( self, name, max_buffer_size = 0 ):
        buffer_size =  self.get_buffersize(max_buffer_size)
        input_char_array = self.crete_input_array(name.encode())
        output_char_array = self.crete_output_array(buffer_size)
        result = self.demangle (input_char_array, output_char_array, buffer_size)
        return result , output_char_array.value

def test():
    name = "_TtuRxs8RunciblerFxWx5Mince6Quince_"
    expected_value = '<A where A: Swift.Runcible>(A) -> A.Mince.Quince'

    result = demangler().get_demangled_name(name)
    if result:
        print(f"demangled successfully but verifying .. ")
        print(f"   {name} ==  {expected_value}")

        if result == expected_value:
            print(f"verification success it returned expected value ")
            print(f"    argument =   {name} \n    result =     {result}")
        else:
            print(f"verification failed .it returned unexpected value")
            print(f"    argument =   {name} \n    result =     {result}")
    else:
        print(f"it is not a mangled swift symbol/function  = {name}")

def get_comandline_args():
    parser = argparse.ArgumentParser(description="this module returns a demangled swift symbol name if given mangled symbol name as input")
    parser.add_argument("-n", "--name", help = "provide mangled swift symbol")
    parser.add_argument("-t", "--test",nargs='?', help="use this parameter to test hardcoded value  ", type=str, default='',required=False)
    args = parser.parse_args()
    return args ,parser

if __name__ == "__main__":
    args,parser = get_comandline_args()

    if args.name :
        result = demangler().get_demangled_name(args.name)
        if result:
            print(result)
        else:
            print("")
            sys.stderr.writelines(f"it is not a mangled swift symbol/function")
        
    elif  args.test :
        test()

    else:
        parser.print_help()



