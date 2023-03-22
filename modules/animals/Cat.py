# -*- coding: utf-8 -*-
# @Author: Arunabh Sharma
# @Date:   2023-03-22 13:24:27
# @Last Modified by:   Arunabh Sharma
# @Last Modified time: 2023-03-22 16:50:00

from Animal import *


class Cat(Animal):
    """Feline Child of the animal class
    """

    def __init__(self, name, num_limbs=4):
        """Constructor for the Cat class

        Args:
            name (str): Name of the Cat
            num_limbs (int, optional): Number of limbs of the Cat
        """
        super().__init__(name, num_limbs)

    def talk(self):
        """Getter for sounds the Cat makes

        Returns:
            str: Sounds the Cat makes in text form 
        """
        return f"{self.name} says: Meow!"
