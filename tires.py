# -*- coding: utf-8 -*-
"""
Concrete tire set classes.

For the purposes of Task 4 of Lyft's VE.

Created on 02/May/2022 -- 04:37
@author: Shipkaliev
"""

from classes import TireSet


class CarriganTires(TireSet):
    """A Carrigan tire set."""

    def __init__(self, tires_wear):
        self._tires_wear = tires_wear

    def needs_service(self) -> bool:
        return any(
            [wear_value >= 0.9 for wear_value in self._tires_wear]
        )


class OctoprimeTires(TireSet):
    """An Octoprime tire set."""

    def __init__(self, tires_wear):
        self._tires_wear = tires_wear

    def needs_service(self) -> bool:
        return sum(self._tires_wear) >= 3
