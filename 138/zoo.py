class Animal:
    _animals = []
    _IDX_BASE = 10001

    def __init__(self, name):
        self._name = name
        self._animals.append(self)

    def __str__(self):
        idx = self._animals.index(self) + self._IDX_BASE
        return f"{idx}. {self._name.title()}"

    @classmethod
    def zoo(cls):
        return "\n".join(
            [
                f"{idx}. {animal._name.title()}"
                for idx, animal in enumerate(cls._animals, cls._IDX_BASE)
            ]
        )


if __name__ == "__main__":
    dog = Animal("dog")
    cat = Animal("cat")
    fish = Animal("fish")
    lion = Animal("lion")
    mouse = Animal("mouse")
    print([f"{animal}" for animal in Animal._animals])
    print(Animal.zoo())
