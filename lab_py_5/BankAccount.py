from abc import ABC, abstractmethod


class Date:
    year = 1900
    month = 1
    day = 1

    def __init__(self, day=1, month=1, year=1900):
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
    def add_balance(self, a):
        pass

    @abstractmethod
    def sub_balance(self, a):
        pass


class CurrentAccount(BankAccount):
    last_operation_date = Date()
    balance = 0.0

    def __init__(self, attributes):
        super(CurrentAccount, self).__init__(attributes)
        self.balance = attributes[2]
        self.last_operation_date = Date()

    def set_last_operation_date(self, date):
        self.last_operation_date = date

    def get_last_operation_date(self):
        return self.last_operation_date

    def get_balance(self):
        return self.balance

    def add_balance(self, a):
        self.balance += a

    def sub_balance(self, a):
        self.balance -= a


class DepositAccount(BankAccount):
    opening_date = Date()
    period = 0
    balance = 0.0
    rate = 0.0

    def __init__(self, attributes):
        super(DepositAccount, self).__init__(attributes)
        self.balance = attributes[2]
        self.rate = attributes[3]
        att_for_date = attributes[4].split('.')
        self.opening_date = Date(att_for_date[0], att_for_date[1], att_for_date[2])
        self.period = attributes[5]

    def get_opening_date(self):
        return self.opening_date

    def get_period(self):
        return self.period

    def get_balance(self):
        return self.balance

    def get_rate(self):
        return self.rate

    def add_balance(self, a):
        self.balance += a

    def sub_balance(self, a):
        self.balance -= a
