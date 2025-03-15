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

import colorsys
import time
import tranci


def main():
    print(tranci.Red("This is red text"))
    print(tranci.Green("This is green text"))
    print(tranci.Blue("This is blue text"))

    print(tranci.BrightRed("This is bright red text"))
    print(tranci.BrightGreen("This is bright green text"))
    print(tranci.BrightBlue("This is bright blue text"))

    print(tranci.BGRed("This text has a red background"))
    print(tranci.BGGreen("This text has a green background"))
    print(tranci.BGBlue("This text has a blue background"))

    print(tranci.BGBrightRed("This text has a bright red background"))
    print(tranci.BGBrightGreen("This text has a bright green background"))
    print(tranci.BGBrightBlue("This text has a bright blue background"))

    print(tranci.Bold(tranci.Red("This is bold and red text")))
    print(tranci.Italicized(tranci.Green("This is italicized and green text")))
    print(tranci.Underlined(tranci.Blue("This is underlined and blue text")))

    print(
        tranci.Red(
            f"This is red text, but {tranci.Blue('this is blue')}. And the rest is red."
        )
    )

    print(tranci.RGB("This is custom RGB color text", 255, 165, 0))
    print(
        tranci.Bold(
            tranci.Italicized(
                tranci.Underlined(
                    tranci.BrightMagenta(
                        "This is bold, italicized, underlined, and bright magenta text"
                    )
                )
            )
        )
    )

    for hue in range(360):
        r, g, b = colorsys.hsv_to_rgb(hue / 360, 1, 1)
        r, g, b = r * 255, g * 255, b * 255
        print(tranci.RGB(f"Rainbow!!", r, g, b), end="\r")
        time.sleep(0.005)

    print()


if __name__ == "__main__":
    main()
