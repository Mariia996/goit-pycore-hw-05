from typing import Callable, Generator, Any
from decimal import Decimal
import re


def generator_numbers(text: str) -> Generator[float | int, Any, None]:
    """
    generator_numbers function finds all numbers in the text and
    return each number as a generator.
    """
    pattern = r"\s(\d+\.?\d+?)\s"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number


def sum_profit(text: str, func: Callable) -> Decimal:
    """
    sum_profit function calculates profit sum by taking each value from
    the numbers generator.
    """
    sum = 0
    for number in func(text):
        sum = Decimal(number) + Decimal(sum)

    return sum.quantize(Decimal("0.00"))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
