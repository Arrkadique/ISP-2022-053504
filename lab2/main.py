import inspect
import yaml
from yaml.loader import Loader
from ArrkadiqueSerializer.serializers.YamlSerializer import YamlSerializer
from ArrkadiqueSerializer.serializers.TomlSerializer import TomlSerializer
from ArrkadiqueSerializer.serializers.JsonSerializer import JsonSerializer
from ArrkadiqueSerializer.parsers.JsonParser import JsonParser

import math

c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)

def faweq():
    a = 125
    print(a)

class asdf:
    __we = None

    def __init__(self, qwe):
        self.__we = qwe


class QWErwq:
    __a = 0
    __b = "123123"
    __c = {}

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def qwer(self):
        print(123)


def main():
    dict_sample = {}

    qwe = QWErwq(25, "12313", dict_sample)
    a = asdf(qwe)


    ser = JsonSerializer()
    prs = JsonParser()

    with open("/home/arkady/dev/data.txt", "w") as file:
        file.write(ser.dumps(faweq))
        file.close()

    with open("/home/arkady/dev/data.txt", "r") as file:
        qweeqweqwe = ser.loads(file.read())
        faweq()
        qweeqweqwe()
        file.close()


if __name__ == "__main__":
    main()
