from abc import ABC


class Course:
    def __set_name__(self, owner, name):
        self.name = '_' + name


    def __set__(self, instance, value):
        if isinstance(value, dict):
            setattr(type(self), self.name, value)
        else:
            getattr(type(self), self.name)[instance.currency] = value


    def __get__(self, instance, owner):
        if not hasattr(type(self), self.name):
            setattr(type(self), self.name, {'': 60, '$': 1.2, '€': 1})
        return getattr(type(self), self.name)


class Currency(ABC):
    course = Course()


    def __init__(self, amount) -> None:
        self.amount = amount


    def __str__(self):
        return f"{self.amount} {self.currency}"

    
    def __add__(self, other):
        """
        Сложение валют.

        Args:
            other (Currency): Другая валюта.

        Returns:
            Currency: Результат сложения валют.
        """
        return type(self)(self.amount + other.to(type(self)).amount)
        

    def __sub__(self, other):
        """
        Вычитание валют.

        Args:
            other (Currency): Другая валюта.

        Returns:
            Currency: Результат вычитания валют.
        """
        return type(self)(self.amount - other.to(type(self)).amount)


    def __mul__(self, number):
        """
        Умножение валюты на число.

        Args:
            number (float): Число для умножения.

        Returns:
            Currency: Результат умножения валюты на число.
        """
        return type(self)(self.amount * number)


    def __truediv__(self, number):
        """
        Деление валюты на число.

        Args:
            number (int): Число для деления.

        Returns:
            Currency: Результат деления валюты на число.
        """
        return type(self)(self.amount / number)


    def __eq__(self, other):
        """
        Сравнение валют по сумме.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если суммы равны, иначе False.
        """
        return self.amount == other.to(type(self)).amount


    def __lt__(self, other):
        """
        Сравнение валют: меньше чем.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта меньше другой, иначе False.
        """
        return self.amount < other.to(type(self)).amount


    def __gt__(self, other):
        """
        Сравнение валют: больше чем.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта больше другой по сумме, иначе False.
        """
        return self.amount > other.to(type(self)).amount


    def __le__(self, other):
        """
        Сравнение валют: меньше или равно.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта меньше или равна другой по сумме, иначе False.
        """
        return self.amount <= other.to(type(self)).amount


    def __ge__(self, other):
        """
        Сравнение валют: больше или равно.

        Args:
            other (Currency): Другая валюта.

        Returns:
            bool: True, если данная валюта больше или равна другой по сумме, иначе False.
        """
        return self.amount >= other.to(type(self)).amount
        

    def to(self, other_cls):
        diff = self.course[other_cls.currency] / self.course[self.currency]
        return other_cls(self.amount * diff)


class Euro(Currency): currency = '€'
class Dollar(Currency): currency = '$'
class Ruble(Currency): currency = ''


e = Euro(5)
d = Dollar(0)
print(e)
# 5 €
print(e.to(Dollar))
# 6 $
print(sum([Euro(i).amount for i in range(5)]))
# 10 €
print(e > Euro(6))
# False
print(e + Dollar(10))
# 13 €
print(Dollar(10) + e)
# 16 $
d.course = 2 # установили курс евро в два доллара
print(e.to(Dollar))
# 10 $
print(Euro.course[Dollar.currency])
# 2
print(Euro.course[Ruble.currency])
# 60
print(e.currency)
# 'Euro'
