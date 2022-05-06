import math
from serializers.create_serializer import create_serializer

my_dict = {
    "qwe": 123,
    "qwe1": 123124,
    "123": "q23124"
}

class a:
    qwe = 234

    def _show(self):
        return self.qwe + 2042


c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)

def main():
    mytoml = create_serializer("toml")
    myyaml = create_serializer("yaml")
    myjson = create_serializer("json")
    with open("/home/arkady/dev/data.toml", "w") as file:
        file.write(mytoml.dumps(f))
        file.close()
    print(mytoml.load("/home/arkady/dev/data.toml")(1))

    myyaml.dump(a, "/home/arkady/dev/data.yaml")
    serclass = myyaml.load("/home/arkady/dev/data.yaml")
    print(serclass.qwe)
    print(serclass._show(serclass))

    myjson.dump(my_dict, "/home/arkady/dev/data.json")
    print(myjson.load("/home/arkady/dev/data.json"))


if __name__ == "__main__":
    main()
