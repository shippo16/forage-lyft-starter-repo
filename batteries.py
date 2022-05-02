# -*- coding: utf-8 -*-
"""
Concrete car battery classes.

For the purposes of Task 2 of Lyft's VE.

Created on 01/May/2022 -- 23:25
@author: Shipkaliev
"""

from datetime import date

from classes import Battery


class SpindlerBattery(Battery):
    """A Spindler car battery."""

    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self) -> bool:
        service_threshold = 365 * 3  # 3 years in days
        time_since_last_service = self._current_date - self._last_service_date  # type: datetime.timedelta
        return time_since_last_service.days > service_threshold


class NubbinBattery(Battery):
    """A Nubbin car battery."""

    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self) -> bool:
        service_threshold = 365 * 4  # 4 years in days
        time_since_last_service = self._current_date - self._last_service_date  # type: datetime.timedelta
        return time_since_last_service.days > service_threshold