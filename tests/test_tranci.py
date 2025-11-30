import tranci

RESET: str = tranci.RESET


def test_basic_color() -> None:
    assert str(tranci.Red("hi")) == "\x1b[31mhi\033[0m"
    assert str(tranci.Blue("x")) == "\x1b[34mx\033[0m"


def test_color_call() -> None:
    r = tranci.Green
    assert r("ok") == "\x1b[32mok\033[0m"
    g = tranci.RGB(123,123,123)
    assert g.code == "\033[38;2;123;123;123m"
    assert g("world") == "\033[38;2;123;123;123mworld\033[0m"


def test_nested_styles() -> None:
    bold = tranci.Bold("yo")
    assert bold.startswith("\x1b[1m")
    assert bold.endswith(RESET)


def test_newline_resets() -> None:
    assert tranci.Red("a\nb") == "\x1b[31ma\033[0m\n\x1b[31mb\033[0m"
    assert tranci.Red("a\r\nb") == "\x1b[31ma\033[0m\r\n\x1b[31mb\033[0m"


def test_rgb() -> None:
    assert tranci.RGB(10, 20, 30, "z") == "\033[38;2;10;20;30mz\033[0m"


def test_hex() -> None:
    assert tranci.HEX("#112233", "x") == "\033[38;2;17;34;51mx\033[0m"
    assert tranci.HEX("112233", "x") == "\033[38;2;17;34;51mx\033[0m"
    assert tranci.HEX(0x112233, "x") == "\033[38;2;17;34;51mx\033[0m"


def test_bg_rgb() -> None:
    assert tranci.BGRGB(1, 2, 3, "k") == "\033[48;2;1;2;3mk\033[0m"


def test_bg_hex() -> None:
    assert tranci.BGHEX("#112233", "x") == "\033[48;2;17;34;51mx\033[0m"
    assert tranci.BGHEX("112233", "x") == "\033[48;2;17;34;51mx\033[0m"
    assert tranci.BGHEX(0x112233, "x") == "\033[48;2;17;34;51mx\033[0m"


def test_hyperlink() -> None:
    assert tranci.Hyperlink("https://example.com", "click") == \
           "\033]8;;https://example.com\033\\click\033]8;;\033"


def test_cursor_dir() -> None:
    assert tranci.move_cursor_dir(tranci.Direction.UP, 3, do_print=False) == "\033[3A"


def test_cursor_pos() -> None:
    assert tranci.move_cursor_pos(5, 10, do_print=False) == "\033[5;10H"


def test_cursor_visibility() -> None:
    assert tranci.set_cursor_visibility(True, do_print=False) == "\033[?25h"
    assert tranci.set_cursor_visibility(False, do_print=False) == "\033[?25l"


def test_clear_screen() -> None:
    assert tranci.clear_screen(do_print=False) == "\033[2J"


def test_clear_line() -> None:
    assert tranci.clear_line(do_print=False) == "\033[2K"


def test_nesting() -> None:
    assert tranci.Blue(f"blue text {tranci.Red('RED TEXT JUMPSCARE')} nvm blue again") == \
           "\x1b[34mblue text \x1b[31mRED TEXT JUMPSCARE\x1b[34m nvm blue again\x1b[0m"
    assert tranci.Red(tranci.Underlined(tranci.Italicized(tranci.Blue(tranci.Bold("wtf"))))) == \
           "\x1b[31m\x1b[4m\x1b[3m\x1b[34m\x1b[1mwtf\x1b[34m\x1b[3m\x1b[4m\x1b[31m\x1b[0m"


def test_weird_input() -> None:
    assert tranci.Red(1) == "\x1b[31m1\x1b[0m"  # type: ignore
    assert tranci.Red(4.3) == "\x1b[31m4.3\x1b[0m"  # type: ignore
    assert tranci.Red([1, 2, 3]) == "\x1b[31m[1, 2, 3]\x1b[0m"  # type: ignore
