"""Core demangler implementation."""

import ctypes
import os

MAX_SYMBOL_LENGTH = 4096  # maximum buffer size for ctypes array.


class demangler:
    """Swift symbol demangler using the official Swift DLL.
    
    This class wraps the Swift DLL's demangling functionality to provide
    Python-friendly access to Swift symbol name demangling.
    
    Args:
        path (str, optional): Path to the swiftDemangle.dll. Defaults to
            the bundled DLL in the package lib directory.
    """

    libname = r"lib/swiftDemangle.dll"
    default_path = os.path.normpath(
        os.path.join(os.path.dirname(__file__), libname)
    )

    def __init__(self, path=""):
        """Initialize the demangler with a Swift DLL.
        
        Args:
            path (str, optional): Path to swiftDemangle.dll. If not provided,
                uses the bundled DLL.
                
        Raises:
            OSError: If the DLL cannot be loaded.
        """
        self.dll_path = path or self.default_path
        try:
            self.libswift = ctypes.WinDLL(self.dll_path)
        except OSError as e:
            raise OSError(
                f"Failed to load Swift DLL from {self.dll_path}. "
                f"Ensure the DLL exists and is accessible. Error: {e}"
            ) from e
        
        self.demangle = self.libswift.fnd_get_demangled_name
        self.demangle.restype = ctypes.c_int
        self.demangle.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]

    def get_buffersize(self, max_buffer_size):
        """Get the buffer size for output.
        
        Args:
            max_buffer_size (int): User-specified buffer size.
            
        Returns:
            int: The buffer size to use.
        """
        return max_buffer_size or MAX_SYMBOL_LENGTH

    def create_input_array(self, name):
        """Create a ctypes buffer for input.
        
        Args:
            name (bytes): The mangled symbol name as bytes.
            
        Returns:
            ctypes array: Buffer containing the input data.
        """
        char_array = (ctypes.c_char * (len(name) + 1))()
        ctypes.memmove(char_array, name, len(name))
        return char_array

    def create_output_array(self, buffer_size):
        """Create a ctypes buffer for output.
        
        Args:
            buffer_size (int): Size of the output buffer.
            
        Returns:
            ctypes array: Empty buffer for output data.
        """
        char_array = (ctypes.c_char * buffer_size)()
        return char_array

    def get_demangled_name(self, name, max_buffer_size=0):
        """Get the demangled name for a Swift symbol.
        
        Args:
            name (str): The mangled Swift symbol name.
            max_buffer_size (int, optional): Maximum buffer size for output.
                Defaults to 0 (uses MAX_SYMBOL_LENGTH).
                
        Returns:
            str or None: The demangled symbol name, or None if demangling fails.
        """
        result_length, val = self._normalize(name, max_buffer_size)
        if result_length:
            target_output_buffer_length = self.get_buffersize(max_buffer_size)
            if result_length > target_output_buffer_length:
                # If result is greater than buffer, rerun with larger buffer
                result_length, val = self._normalize(
                    name, max_buffer_size=result_length + 1
                )
            return val.decode()
        return None

    def _normalize(self, name, max_buffer_size=0):
        """Internal method to call the DLL and get demangled output.
        
        Args:
            name (str): The mangled symbol name.
            max_buffer_size (int): Buffer size for output.
            
        Returns:
            tuple: (result_length, output_value) from the DLL call.
        """
        buffer_size = self.get_buffersize(max_buffer_size)
        input_char_array = self.create_input_array(name.encode())
        output_char_array = self.create_output_array(buffer_size)
        result = self.demangle(input_char_array, output_char_array, buffer_size)
        return result, output_char_array.value
