# -*- coding: utf-8 -*-
# @Author: Arunabh Sharma
# @Date:   2023-03-22 13:08:35
# @Last Modified by:   Arunabh Sharma
# @Last Modified time: 2023-03-22 14:19:11


class Animal:
    """Animal base class
    """

    def __init__(self, name, num_limbs):
        """Constructor for the Animal class

        Args:
            name (TYPE): Name of the animal
            num_limbs (TYPE): Number of limbs of the animal
        """
        self.name = name
        self.num_limbs = num_limbs

    def talk(self):
        """Getter for the sounds of the animal

        Raises:
            NotImplementedError: Must be implemented in the subclass
        """
        raise NotImplementedError("Subclass must implement talk method")

    def limbs(self):
        """Getter for the number of limbs of the animal

        Returns:
            TYPE: The number of limbs of the animal
        """
        return self.num_limbs

    def name(self):
        """Getter for the name of the animal

        Returns:
            TYPE: The name of the animal
        """
        return self.num_limbs