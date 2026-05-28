import math

class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник раціонального числа не може дорівнювати нулю."):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message="Некоректні дані для операції з раціональним числом."):
        super().__init__(message)

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str) and '/' in n:
            parts = n.split('/')
            n, d = int(parts[0]), int(parts[1])

        if d == 0:
            raise RationalError()

        gcd = math.gcd(n, d)
        self.n = n // gcd
        self.d = d // gcd

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if not isinstance(other, Rational):
            raise RationalValueError(f"Спроба додати некоректний тип '{type(other).__name__}'. Очікується Rational або int.")

        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __str__(self):
        return f"{self.n}/{self.d}"

class RationalList:
    def __init__(self):
        self.items = []

    def append(self, item):
        if not isinstance(item, Rational):
            raise RationalValueError(f"До RationalList можна додавати лише об'єкти Rational. Отримано некоректні дані типу '{type(item).__name__}'.")
        self.items.append(item)

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other.items:
                self.append(item)
        elif isinstance(other, (Rational, int)):
            if isinstance(other, int):
                other = Rational(other)
            self.append(other)
        else:
             raise RationalValueError(f"Неможливо застосувати += до RationalList з типом '{type(other).__name__}'.")
        return self

    def __str__(self):
        return "[" + ", ".join(str(item) for item in self.items) + "]"

if __name__ == "__main__":
    try:
        r1 = Rational(5, 0)
    except RationalError as e:
        print(f"Спіймано виняток: {e}")

    try:
        r2 = Rational(1, 2)
        res = r2 + "рядок"
    except RationalValueError as e:
        print(f"Спіймано виняток: {e}")

    r_list = RationalList()
    r_list.append(Rational(3, 4))
    try:
        r_list.append(3.14)
    except RationalValueError as e:
        print(f"Спіймано виняток: {e}")