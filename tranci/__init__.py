"""
Tranci: a no-dependencies, lightweight, easy-to-use ANSI library

Copyright (c) 2025 Butterroach

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import sys
from typing import Union

if sys.platform == "win32":
    os.system("")  # fix ANSI on conhost

RESET = "\033[0m"

__version__ = "1.0.0"


class BaseText(str):
    """
    Base class for colors and styles. Does not include operations.
    """

    def __new__(cls, code: str, text: Union[str, None] = None):
        if text is None:
            return super().__new__(cls)
        return super().__new__(cls, code + text.replace(RESET, code) + RESET)

    def __init__(self, code: str, text: str = None):
        self.code = code

    def __call__(self, text: str):
        """
        Returns the text provided in the same style. Useful for saving colors and reusing them over and over again.
        """
        return BaseText.__new__(BaseText, self.code, text)


class Bold(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[1m"
        return super().__new__(cls, code, text)


class Dim(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[2m"
        return super().__new__(cls, code, text)


class Italicized(BaseText):
    """
    Some legacy terminals don't support italicized text.
    """

    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[3m"
        return super().__new__(cls, code, text)


class Underlined(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[4m"
        return super().__new__(cls, code, text)


class Blinking(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[5m"
        return super().__new__(cls, code, text)


class SlowlyBlinking(BaseText):
    """
    Support for slow blinking is highly limited. Most modern terminals will treat this the same as normal blink.
    """

    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[6m"
        return super().__new__(cls, code, text)


class Inverted(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[7m"
        return super().__new__(cls, code, text)


class Hidden(BaseText):
    """
    This has absolutely no use. I don't know why this is in ANSI at all.
    """

    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[8m"
        return super().__new__(cls, code, text)


class Striked(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[9m"
        return super().__new__(cls, code, text)


class Black(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[30m"
        return super().__new__(cls, code, text)


class Red(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[31m"
        return super().__new__(cls, code, text)


class Green(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[32m"
        return super().__new__(cls, code, text)


class Yellow(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[33m"
        return super().__new__(cls, code, text)


class Blue(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[34m"
        return super().__new__(cls, code, text)


class Magenta(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[35m"
        return super().__new__(cls, code, text)


class Cyan(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[36m"
        return super().__new__(cls, code, text)


class White(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[37m"
        return super().__new__(cls, code, text)


class Gray(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[90m"
        return super().__new__(cls, code, text)


class BrightRed(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[91m"
        return super().__new__(cls, code, text)


class BrightGreen(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[92m"
        return super().__new__(cls, code, text)


class BrightYellow(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[93m"
        return super().__new__(cls, code, text)


class BrightBlue(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[94m"
        return super().__new__(cls, code, text)


class BrightMagenta(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[95m"
        return super().__new__(cls, code, text)


class BrightCyan(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[96m"
        return super().__new__(cls, code, text)


class BrightWhite(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[97m"
        return super().__new__(cls, code, text)


class BGBlack(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[40m"
        return super().__new__(cls, code, text)


class BGRed(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[41m"
        return super().__new__(cls, code, text)


class BGGreen(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[42m"
        return super().__new__(cls, code, text)


class BGYellow(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[43m"
        return super().__new__(cls, code, text)


class BGBlue(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[44m"
        return super().__new__(cls, code, text)


class BGMagenta(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[45m"
        return super().__new__(cls, code, text)


class BGCyan(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[46m"
        return super().__new__(cls, code, text)


class BGWhite(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[47m"
        return super().__new__(cls, code, text)


class BGGray(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[100m"
        return super().__new__(cls, code, text)


class BGBrightRed(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[101m"
        return super().__new__(cls, code, text)


class BGBrightGreen(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[102m"
        return super().__new__(cls, code, text)


class BGBrightYellow(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[103m"
        return super().__new__(cls, code, text)


class BGBrightBlue(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[104m"
        return super().__new__(cls, code, text)


class BGBrightMagenta(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[105m"
        return super().__new__(cls, code, text)


class BGBrightCyan(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[106m"
        return super().__new__(cls, code, text)


class BGBrightWhite(BaseText):
    def __new__(cls, text: Union[str, BaseText, None] = None):
        code = "\033[107m"
        return super().__new__(cls, code, text)


class RGB(BaseText):
    def __new__(cls, r: int, g: int, b: int, text: Union[str, BaseText, None] = None):
        return super().__new__(cls, f"\033[38;2;{int(r)};{int(g)};{int(b)}m", text)

    def __init__(self, r: int, g: int, b: int, text: Union[str, BaseText, None] = None):
        self.code = f"\033[38;2;{int(r)};{int(g)};{int(b)}m"


class HEX(RGB):
    def __new__(cls, hexa: Union[str, int], text: Union[str, BaseText, None] = None):
        if isinstance(hexa, str):
            hexa = int(hexa.replace("#", ""), 16)
        return super().__new__(
            cls, (hexa >> 16) & 255, (hexa >> 8) & 255, hexa & 255, text
        )

    def __init__(self, hexa: Union[str, int], text: Union[str, BaseText, None] = None):
        if isinstance(hexa, str):
            hexa = int(hexa.replace("#", ""), 16)
        super().__init__((hexa >> 16) & 255, (hexa >> 8) & 255, hexa & 255)


class BGRGB(BaseText):
    def __new__(cls, r: int, g: int, b: int, text: Union[str, BaseText, None] = None):
        return super().__new__(cls, f"\033[48;2;{int(r)};{int(g)};{int(b)}m", text)

    def __init__(self, r: int, g: int, b: int, _=None):
        self.code = f"\033[48;2;{int(r)};{int(g)};{int(b)}m"


class BGHEX(BGRGB):
    def __new__(cls, hexa: Union[str, int], text: Union[str, BaseText, None] = None):
        if isinstance(hexa, str):
            hexa = int(hexa.replace("#", ""), 16)
        return super().__new__(
            cls, (hexa >> 16) & 255, (hexa >> 8) & 255, hexa & 255, text
        )

    def __init__(self, hexa: Union[str, int], text: Union[str, BaseText, None] = None):
        if isinstance(hexa, str):
            hexa = int(hexa.replace("#", ""), 16)
        super().__init__((hexa >> 16) & 255, (hexa >> 8) & 255, hexa & 255)
