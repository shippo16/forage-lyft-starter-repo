# -*- coding: utf-8 -*-
"""
The CarFactory class.

For the purposes of Task 2 of Lyft's VE.

Created on 01/May/2022 -- 23:43
@author: Shipkaliev
"""

from datetime import date

from classes import Car
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from batteries import NubbinBattery, SpindlerBattery


class CarFactory:
    """A car factory class."""

    @classmethod
    def create_calliope(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=SpindlerBattery(current_date, last_service_date)
        )

    @classmethod
    def create_glissade(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=SpindlerBattery(current_date, last_service_date)
        )

    @classmethod
    def create_palindrome(self, current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        return Car(
            engine=SternmanEngine(warning_light_on),
            battery=SpindlerBattery(current_date, last_service_date)
        )

    @classmethod
    def create_rorschach(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(current_date, last_service_date)
        )

    @classmethod
    def create_thovex(self, current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(current_date, last_service_date)
        )
