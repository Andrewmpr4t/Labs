import math
import re

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, Rational):
            self.n = n.n
            self.d = n.d
            return
        
        if isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                n, d = int(parts[0]), int(parts[1])
            else:
                n, d = int(n), 1
                
        if d == 0:
            raise ZeroDivisionError("Знаменник не може дорівнювати нулю.")
            
        gcd = math.gcd(int(n), int(d))
        self.n = (int(n) // gcd) * (1 if int(d) > 0 else -1)
        self.d = abs(int(d) // gcd)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Правим операндом має бути Rational або int")
        return Rational(self.n * other.d + other.n * self.d, self.d * other.d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Правим операндом має бути Rational або int")
        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        return Rational(other.n * self.d - self.n * other.d, self.d * other.d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Правим операндом має бути Rational або int")
        return Rational(self.n * other.n, self.d * other.d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Правим операндом має бути Rational або int")
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль.")
        return Rational(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if self.n == 0:
            raise ZeroDivisionError("Ділення на нуль.")
        return Rational(other.n * self.d, other.d * self.n)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == 'n':
            return self.n
        elif key == 'd':
            return self.d
        raise KeyError("Використовуйте ключі 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == 'n':
            self.n = value
        elif key == 'd':
            if value == 0:
                raise ZeroDivisionError("Знаменник не може дорівнювати нулю.")
            self.d = value
        else:
            raise KeyError("Використовуйте ключі 'n' або 'd'")
            
        gcd = math.gcd(self.n, self.d)
        self.n = (self.n // gcd) * (1 if self.d > 0 else -1)
        self.d = abs(self.d // gcd)

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else str(self.n)
        
    def __repr__(self):
        return self.__str__()


def evaluate_expressions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    expressions = []
    current_expr = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        current_expr += " " + line
        if current_expr.strip()[-1] not in "+-*/":
            expressions.append(current_expr.strip())
            current_expr = ""

    print("=== Результати обчислень ===")
    for i, expr in enumerate(expressions, 1):
        python_expr = re.sub(r'\b\d+(?:/\d+)?\b', lambda m: f"Rational('{m.group(0)}')", expr)
        
        try:
            result = eval(python_expr)
            print(f"\nВираз {i}: {expr}")
            print(f"Раціональний результат: {result}")
            print(f"Десятковий результат:   {result()}")
        except Exception as e:
            print(f"\nВираз {i}: {expr}")
            print(f"Помилка обчислення: {e}")

if __name__ == '__main__':
    evaluate_expressions_from_file('input01.txt')