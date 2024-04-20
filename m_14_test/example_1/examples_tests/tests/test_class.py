import unittest
from pathlib import Path  # Importing pathlib correctly

# Dynamically adding 'src' directory to the Python path
import sys

project_root = (
    Path(__file__).resolve().parents[1]
)  # Go two levels up to reach the project root
sys.path.append(str(project_root))

src_path = str(Path(__file__).resolve().parent.parent.joinpath("src"))
hw_path = Path(__file__)
print(f"{hw_path=}")
print(f"{src_path=}")
print(f"{project_root=}")
from src.my_class.main import Cat, CatDog, Dog, DogCat, Animal


class TestClass(unittest.TestCase):

    def test_dog(self):
        self.assertEqual(Dog.__base__, Animal, msg='Class Dog not inherit class Animal')

    def test_cat_dog(self):
        assert Dog in CatDog.__bases__, 'Class Dog must be parent for class CatDog'  # raise AssertionError('Class Dog must be parent for class CatDog')
        assert 'info' in dir(CatDog), 'Not implemented method info'
        
if __name__ == "__main__":
    unittest.main()
