from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        self.title = self.title.capitalize()


if __name__ == "__main__":
    b1 = Bite(number=1, title="sum of numbers")
    b3 = Bite(number=3, title="a hard bite", level="Advanced")
    b2 = Bite(number=2, title="a second bite", level="Intermediate")
    bites = [b1, b2, b3]
    print(bites)
