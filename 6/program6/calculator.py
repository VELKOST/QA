class Calculator:
    def add(self, *args):
        """Суммирует произвольное количество чисел."""
        total = 0
        for x in args:
            total += x
        return total

    def divide(self, a, b):
        """Делит a на b. Должен бросать ZeroDivisionError при b == 0."""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    def is_prime_number(self, n: int) -> bool:
        """Проверяет, является ли n простым числом (n >= 2)."""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
