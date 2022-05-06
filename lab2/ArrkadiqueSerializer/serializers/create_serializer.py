from ArrkadiqueSerializer.serializers.JsonSerializer import JsonSerializer
from ArrkadiqueSerializer.serializers.YamlSerializer import YamlSerializer
from ArrkadiqueSerializer.serializers.TomlSerializer import TomlSerializer
from ArrkadiqueSerializer.serializers.BaseSerializer import BaseSerializer

SERIALIZERS_MAP = {
    "json": JsonSerializer,
    "toml": TomlSerializer,
    "yaml": YamlSerializer
}


def create_serializer(exten_name: str) -> BaseSerializer:
    if exten_name in SERIALIZERS_MAP:
        return SERIALIZERS_MAP[exten_name]()
    else:
        return None
