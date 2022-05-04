import imp
import inspect
import sys
from types import CodeType, ModuleType


def get_globals(obj) -> dict:
    result = {}
    for glob in obj.__globals__.items():
        if glob[0] in obj.__code__.co_names:
            result.update({glob[0]: glob[1]})
    return result


def get_code_fields(_code: CodeType) -> dict:
    result = {}
    for member in inspect.getmembers(_code):
        if str(member[0]).startswith("co_"):
            result.update({member[0]: member[1]})
    return result


def get_actual_module_fields(module: ModuleType) -> dict:
    module_fields = {}
    module_members = inspect.getmembers(module)
    for mem in module_members:
        if not mem[0].startswith("__"):
            module_fields.update({mem[0]: mem[1]})
    return module_fields


def is_std_lib_module(module: ModuleType):
    python_libs_path = sys.path[2]
    module_path = imp.find_module(module.__name__)[1]
    if module.__name__ in sys.builtin_module_names:
        return True
    elif python_libs_path in module_path:
        return True
    elif 'site-packages' in module_path:
        return True
    return False
