import inspect
import re
from types import CodeType, ModuleType, FunctionType

import yaml

from ..dto.DTO import DTO
from ..dto.DTO import DTO_TYPES
from .. import attributes
from ArrkadiqueSerializer.parsers import YamlParser


class YamlSerializer():

    __buf = 0
    __gap = 0
    __is_blocked_gaps = False
    __result = ""
    __parser = None

    def __init__(self):
        self.__parser = YamlParser.YamlParser()

    def dump(self, obj, filepath):
        with open(filepath, "w") as file:
            file.write(self.dumps(obj))

    def dumps(self, obj):
        return self._serialize(obj)

    def loads(self, source: str) -> any:
        return self.__parser.parse(source)

    def load(self, file_path: str) -> any:
        obj = None
        with open(file_path) as file:
            _str = file.read()
            obj = self.loads(_str)
        return obj

    def _serialize(self, obj) -> str:
        return yaml.dump(self._choosing_type(obj), sort_keys=False)

    def _choosing_type(self, obj):
        if type(obj) in (int, float, bool, str, bytes, type(None)):
            res = obj
        elif type(obj) in (tuple, list):
            res = self._ser_list(obj)
        elif type(obj) == dict:
            res = self._ser_dict(obj)
        elif type(obj) == FunctionType:
            res = self._ser_func(obj)
        elif type(obj) == ModuleType:
            res = self._ser_module(obj)
        return res

    def _ser_list(self, obj) -> list:
        res = []
        for a in obj:
            res.append(self._choosing_type(a))
        return res

    def _ser_dict(self, obj) -> dict:
        res = {}
        res[f'{DTO.dto_type}'] = f'{DTO_TYPES.DICT}'
        for a in obj.items():
            res[self._choosing_type(a[0])] = self._choosing_type(a[1])
        return res

    def _ser_func(self, obj: FunctionType) -> dict:
        res = {}
        res[f'{DTO.dto_type}'] = f'{DTO_TYPES.FUNC}'
        res[f'{DTO.name}'] = self._choosing_type(obj.__name__)
        res[f'{DTO.global_names}'] = self._choosing_type(attributes.get_globals(obj))
        res[f'{DTO.code}'] = self._choosing_type(attributes.get_code_fields(obj.__code__))
        res[f'{DTO.closure}'] = self._choosing_type(obj.__closure__)
        return res

    def _ser_module(self, obj: ModuleType) -> dict:
        res = {}
        res[f'{DTO.dto_type}'] = f'{DTO_TYPES.MODULE}'
        res[f'{DTO.name}'] = self._choosing_type(obj.__name__)
        if attributes.is_std_lib_module(obj):
            res[f'{DTO.fields}'] = self._choosing_type(None)
        else:
            res[f'{DTO.fields}'] = self._choosing_type(attributes.get_actual_module_fields(obj))
        return res
