# -*- coding: utf-8 -*-
# @Author: Arunabh Sharma
# @Date:   2023-03-22 14:28:45
# @Last Modified by:   Arunabh Sharma
# @Last Modified time: 2023-03-22 14:33:14

import sys
import os
import pytest

sys.path.insert(0, os.path.abspath("../modules/Animals"))  # NOQA
sys.path.insert(0, os.path.abspath("modules/Animals"))  # NOQA

from animals import Animal, Cat, Dog


def test_animal_init():
    animal = Animal("Generic", 4)
    assert animal.name == "Generic"
    assert animal.num_limbs == 4


def test_animal_talk():
    animal = Animal("Generic", 4)
    with pytest.raises(NotImplementedError):
        animal.talk()


def test_animal_limbs():
    animal = Animal("Generic", 4)
    assert animal.limbs() == 4


def test_cat_init():
    cat = Cat("Fluffy")
    assert cat.name == "Fluffy"
    assert cat.num_limbs == 4


def test_cat_talk():
    cat = Cat("Fluffy")
    assert cat.talk() == "Fluffy says: Meow!"


def test_cat_limbs():
    cat = Cat("Fluffy")
    assert cat.limbs() == 4


def test_dog_init():
    dog = Dog("Buddy")
    assert dog.name == "Buddy"
    assert dog.num_limbs == 4


def test_dog_talk():
    dog = Dog("Buddy")
    assert dog.talk() == "Buddy says: Woof!"


def test_dog_limbs():
    dog = Dog("Buddy")
    assert dog.limbs() == 4