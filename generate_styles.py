"""
tranci: a no-dependencies, lightweight, easy-to-use ANSI library

Copyright (c) 2025-2026 Butterroach

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
from typing import Union

STYLE_MAP: dict[str, str] = {
    "Bold": "\033[1m",
    "Dim": "\033[2m",
    "Italicized": "\033[3m",
    "Underlined": "\033[4m",
    "Blinking": "\033[5m",
    "SlowlyBlinking": "\033[6m",
    "Inverted": "\033[7m",
    "Hidden": "\033[8m",
    "Striked": "\033[9m",
    "Black": "\033[30m",
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Magenta": "\033[35m",
    "Cyan": "\033[36m",
    "White": "\033[37m",
    "Gray": "\033[90m",
    "BrightRed": "\033[91m",
    "BrightGreen": "\033[92m",
    "BrightYellow": "\033[93m",
    "BrightBlue": "\033[94m",
    "BrightMagenta": "\033[95m",
    "BrightCyan": "\033[96m",
    "BrightWhite": "\033[97m",
    "BGBlack": "\033[40m",
    "BGRed": "\033[41m",
    "BGGreen": "\033[42m",
    "BGYellow": "\033[43m",
    "BGBlue": "\033[44m",
    "BGMagenta": "\033[45m",
    "BGCyan": "\033[46m",
    "BGWhite": "\033[47m",
    "BGGray": "\033[100m",
    "BGBrightRed": "\033[101m",
    "BGBrightGreen": "\033[102m",
    "BGBrightYellow": "\033[103m",
    "BGBrightBlue": "\033[104m",
    "BGBrightMagenta": "\033[105m",
    "BGBrightCyan": "\033[106m",
    "BGBrightWhite": "\033[107m",
}

DOCS: dict[str, str] = {
    "Italicized": "Some legacy terminals don't support italicized text.",
    "SlowlyBlinking": "Support for slow blinking is highly limited. Most modern terminals will treat this the same as normal blink.",
    "Hidden": "This has absolutely no use. I don't know why this is in ANSI at all.",
}

def generate_class(name: str, code: str, doc: Union[str, None] = None) -> str:
    docstring = f'    """{doc}"""\n' if doc else ''
    return f'''
class {name}(BaseText):
{docstring}    def __new__(cls, text: Union[str, BaseText, None] = None) -> "{name}":  # NOQA
        code = {code!r}
        return cast("{name}", super().__new__(cls, code, text))
'''.rstrip()

def main() -> None:
    lines = []
    for name, code in STYLE_MAP.items():
        doc = DOCS.get(name)
        lines.append(generate_class(name, code, doc))
    out = "\n\n".join(lines) + "\n"

    Path("tranci/styles.py").write_text(out)

if __name__ == "__main__":
    main()
