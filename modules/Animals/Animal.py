# -*- coding: utf-8 -*-
# @Author: Arunabh Sharma
# @Date:   2023-03-22 13:08:35
# @Last Modified by:   Arunabh Sharma
# @Last Modified time: 2023-03-22 13:09:22


class Animal:
    """Summary

    Attributes:
        name (TYPE): Description
        num_limbs (TYPE): Description
    """

    def __init__(self, name, num_limbs):
        """Summary

        Args:
            name (TYPE): Description
            num_limbs (TYPE): Description
        """
        self.name = name
        self.num_limbs = num_limbs

    def talk(self):
        """Summary

        Raises:
            NotImplementedError: Description
        """
        raise NotImplementedError("Subclass must implement talk method")

    def limbs(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self.num_limbs