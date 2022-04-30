from abc import ABC, abstractmethod
from datetime import datetime


class Date:
    __year = 1900
    __month = 1
    __day = 1

    def __init__(self, day=1, month=1, year=1900):
        self.__day = day
        self.__month = month
        self.__year = year

    def set_year(self, year):
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def set_day(self, day):
        self.__day = day

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def __str__(self):
        return "{}.{}.{}".format(self.__year, self.__month, self.__day)

    def get_month_between_dates(self, other):
        return ((self.__year - other.get_year()) * 12) + self.__month - other.get_month()


class BankAccount(ABC):
    __bank_name = ""
    __id = 0
    __is_available = True

    def __init__(self, attributes):
        self.__bank_name = attributes[0]
        self.__id = int(attributes[1])
        self.__is_available = True

    def set_is_available(self, status):
        self.__is_available = status

    def get_bank_name(self):
        return self.__bank_name

    def get_id(self):
        return self.__id

    def get_is_available(self):
        return self.__is_available

    @abstractmethod
    def add_balance(self, a):
        pass

    @abstractmethod
    def sub_balance(self, a):
        pass


class CurrentAccount(BankAccount):
    __last_operation_date = Date()
    __balance = 0.0

    def __init__(self, attributes):
        super(CurrentAccount, self).__init__(attributes)
        self.__balance = float(attributes[2])
        self.__last_operation_date = Date()

    def set_last_operation_date(self, date):
        self.__last_operation_date = date

    def get_last_operation_date(self):
        return self.__last_operation_date

    def get_balance(self):
        return self.__balance

    def add_balance(self, a):
        self.__balance += a

    def sub_balance(self, a):
        self.__balance -= a


class DepositAccount(BankAccount):
    __opening_date = Date()
    __period = 0
    __balance = 0.0
    __rate = 0.0

    def __init__(self, attributes):
        super(DepositAccount, self).__init__(attributes)
        self.__balance = float(attributes[2])
        self.__rate = float(attributes[3])
        att_for_date = attributes[4].split('.')
        self.__opening_date = Date(int(att_for_date[0]), int(att_for_date[1]), int(att_for_date[2]))
        self.__period = int(attributes[5])

    def get_opening_date(self):
        return self.__opening_date

    def get_period(self):
        return self.__period

    def get_balance(self):
        return self.__balance

    def get_rate(self):
        return self.__rate

    def add_balance(self, a):
        self.__balance += a

    def sub_balance(self, a):
        self.__balance -= a


def init_arrays(size, currents, deposits):
    print("Enter info about accounts in format\n"
          "For current account: [bank name, id, balance]\n"
          "For deposit account: [bank name, id, balance, rate, dd.mm.yyyy, period]\n"
          "and again...")
    for i in range(size):
        attributes = input().split(',')
        currents.append(CurrentAccount(attributes))
        attributes = input().split(',')
        deposits.append(DepositAccount(attributes))
        print()

    return currents, deposits


def check_deposits(size, currents, deposits):
    now = get_system_date()
    for i in range(size):
        open_date = deposits[i].get_opening_date()
        completed_month = now.get_month_between_dates(open_date)
        if completed_month >= deposits[i].get_period():
            percents = deposits[i].get_period() * (deposits[i].get_balance() * deposits[i].get_rate())
            currents[i].add_balance(deposits[i].get_balance())
            deposits[i].sub_balance(deposits[i].get_balance())
            deposits[i].set_is_available(False)
            open_date.set_month(open_date.get_month() + deposits[i].get_period())
        else:
            percents = completed_month * (deposits[i].get_balance() * deposits[i].get_rate())
            open_date.set_month(open_date.get_month() + completed_month)
        while open_date.get_month() > 12:
            open_date.set_year(open_date.get_year() + 1)
            open_date.set_month(open_date.get_month() - 12)
        currents[i].add_balance(percents)
        currents[i].set_last_operation_date(open_date)


def print_accounts(size, currents, deposits):
    print()
    for i in range(size):
        c = currents[i]
        d = deposits[i]
        last_op = c.get_last_operation_date()
        status = "Available" if d.get_is_available() else "Unavailable"
        print("Pair {}:\n"
              "id: {}"
              "\tbank name: {}"
              "\tdate of last operation: {}"
              "\tbalance: {}"
              "\nid: {}"
              "\tbank name: {}"
              "\tstatus: {}"
              "\tbalance: {}\n"
              .format(str(i + 1), c.get_id(), c.get_bank_name(), last_op.__str__(), c.get_balance(),
                      d.get_id(), d.get_bank_name(), status, d.get_balance()))


def get_system_date():
    current_datetime = datetime.now()
    sys_date = Date(current_datetime.day, current_datetime.month, current_datetime.year)
    return sys_date
