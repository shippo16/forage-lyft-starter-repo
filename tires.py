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

    def __init__(self, tire_wear):
        self._tire_wear = wear

    def needs_service(self) -> bool:
        return any(
            [wear_value >= 0.9 for wear_value in self._tire_wear]
        )


class OctoprimeTires(TireSet):
    """A Carrigan tire set."""

    def __init__(self, tire_wear):
        self._tire_wear = wear

    def needs_service(self) -> bool:
        return sum(self._tire_wear) >= 3
