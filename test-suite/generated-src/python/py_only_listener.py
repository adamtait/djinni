# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from single_language_interfaces.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files


from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class PyOnlyListener(with_metaclass(ABCMeta)):

class PyOnlyListenerCallbacksHelper():
    @ffi.callback("void(struct DjinniObjectHandle * )")
    def __delete(c_ptr):
        assert c_ptr in PyOnlyListenerHelper.c_data_set
        PyOnlyListenerHelper.c_data_set.remove(c_ptr)

    @staticmethod
    def _add_callbacks():

        lib.py_only_listener_add_callback___delete(PyOnlyListenerCallbacksHelper.__delete)

PyOnlyListenerCallbacksHelper._add_callbacks()

class PyOnlyListenerHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        # Python Objects can be returned without being wrapped in proxies
        py_handle = lib.get_handle_from_proxy_object_cw__py_only_listener(obj)
        if py_handle:
            assert py_handle in PyOnlyListenerHelper.c_data_set
            aux = ffi.from_handle(ffi.cast("void * ", py_handle))
            lib.py_only_listener___wrapper_dec_ref(obj)
            return aux
        return PyOnlyListenerCppProxy(obj)

    @staticmethod
    def selfToPy(obj):
        assert obj in PyOnlyListenerHelper.c_data_set
        return ffi.from_handle(ffi.cast("void * ",obj))

    @staticmethod
    def fromPy(py_obj):
        if py_obj is None:
            return ffi.NULL
        py_proxy = (py_obj)

        bare_c_ptr = ffi.new_handle(py_proxy)
        PyOnlyListenerHelper.c_data_set.add(bare_c_ptr)
        wrapped_c_ptr = lib.make_proxy_object_from_handle_cw__py_only_listener(bare_c_ptr)
        return wrapped_c_ptr