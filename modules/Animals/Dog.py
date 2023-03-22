# -*- coding: utf-8 -*-
# @Author: Arunabh Sharma
# @Date:   2023-03-22 13:24:45
# @Last Modified by:   Arunabh Sharma
# @Last Modified time: 2023-03-22 14:04:39

from Animal import *


class Dog(Animal):
    """Canine child of the Animal Class
    """

    def __init__(self, name, num_limbs=4):
        """Constructor for the Dog class

        Args:
            name (TYPE): Name of the Dog
            num_limbs (int, optional): Number of limbs of the Dog
        """
        super().__init__(name, num_limbs)

    def talk(self):
        """Getter for sounds the Dog makes

        Returns:
            TYPE: Sounds the Dog makes in text form
        """
        return f"{self.name} says: Woof!"