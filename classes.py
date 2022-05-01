# -*- coding: utf-8 -*-
"""
Base classes for the purposes of Task 2 of Lyft's VE.

Created on 01/May/2022 -- 22:48
@author: Shipkaliev
"""

from abc import ABC, abstractmethod


# Abstract classes:

class Serviceable(ABC):
    """
    An abstract class representing an object that must be serviced at
    some point.
    """

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Engine(Serviceable):
    """An abstract car engine class."""
    pass


class Battery(Serviceable):
    """An abstract car battery class."""
    pass


# Concrete classes:

class Car(Serviceable):
    """A car."""

    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        return self._engine.needs_service() or \
               self._battery.needs_service()
