from abc import ABC, abstractmethod

from setuptools.ssl_support import is_available


class Date:
    year = 1900
    month = 1
    day = 1

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def __str__(self):
        return "{}.{}.{}".format(self.year, self.month, self.day)

    def get_month_between_dates(self, other):
        return ((self.year - other.year) * 12) + self.month - other.month


class BankAccount(ABC):
    bank_name = ""
    id = 0
    is_available = True

    def __init__(self, attributes):
        self.bank_name = attributes[0]
        self.id = attributes[1]
        self.is_available = True

    def set_is_available(self, status):
        self.is_available = status

    def get_bank_name(self):
        return self.bank_name

    def get_id(self):
        return self.id

    def get_is_available(self):
        return self.is_available

    @abstractmethod
    def add_balance(self):
        pass

    @abstractmethod
    def sub_balance(self):
        pass
