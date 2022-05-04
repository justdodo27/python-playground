from typing import Optional, List, Final
from enum import Enum

text = ('abc' 'def', 'xd')
print(text)

class JustDodoClass:
    pass

class JustDodoClassOtherPass:
    ...

def example_match_case(variable: str) -> Optional[int]:
    match variable.lower():
        case 'a' | 'b':
            return 2
        case 'a':
            return 1
        case _:
            return -1 

xd="Kubek z kawią"

print(f"bardzo lubię mój {xd=}")

print(example_match_case("a"))

def example_match_case_list(x: List[str]) -> Optional[int]:
    match x:
        case [_]:
            return 2
        case [_, _,*_]:
            print("At least two items")
            return 1
        case [_, _]:
            print("At least two XD")
            return 1
        case _:
            return -1 

example_match_case_list(["a", "b", "c", "c"])

class Settings(Enum):
    VOLUME: Final[str] = "VOL"
    BRIGHTNESS: Final[str] = "LUX"  # lux!
    KLO = "CUCH"  # miglanc

setting = Settings("LUX")
setting.BRIGHTNESS = "DUPA"  # To jebać

print(setting.BRIGHTNESS)

print(f"Ten log dotyczy: {Settings.VOLUME}")

def foo():

    """X :param: This is my function"""

    pass

print(foo.__doc__)

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""

def func():
    ...

for i, q in enumerate(["a" for _ in range(5)]):
    print(q)

print(i)