from pydantic import RootModel


class Pets(RootModel[list[str]]):
    def describe(self) -> str:
        return f'Pets: {", ".join(self.root)}'


if __name__ == "__main__":
    my_pets = Pets.model_validate(["dog", "cat"])
    print(my_pets.describe())
