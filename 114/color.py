import os
import re
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402

HEX_RGX = re.compile(r"^#[0-9a-fA-F]{6}$")


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = (
            COLOR_NAMES[color.upper()] if (color.upper() in COLOR_NAMES) else None
        )
        self._color = color

    @staticmethod
    def hex2rgb(hex_color):
        """Class method that converts a hex value into an rgb one"""
        if not HEX_RGX.match(hex_color):
            raise ValueError(f"Invalid hex value: {hex}")

        hex_color = hex_color[1:]
        return (
            int(hex_color[:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )

    @staticmethod
    def rgb2hex(rgb_tuple):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb_tuple, tuple):
            raise ValueError(f"Invalid hex value: {rgb_tuple}")
        elif not (
            all((isinstance(v, int) and (0 <= v <= 255) for v in rgb_tuple))
            and (len(rgb_tuple) == 3)
        ):
            raise ValueError(f"Invalid hex value: {rgb_tuple}")

        return f"#{rgb_tuple[0]:02x}{rgb_tuple[1]:02x}{rgb_tuple[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self._color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"


if __name__ == "__main__":
    print(Color("white"))
    print(Color("white").rgb)
    print(repr(Color("Blue")))
    print(Color("white").rgb2hex((255, 255, 255)))
    print(Color.hex2rgb("#ff0006"))
    print(Color.rgb2hex(Color.hex2rgb("#ff0006")))
