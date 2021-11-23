def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""

    if not all((0 <= v <= 255 for v in rgb)):
        raise ValueError(f"Invalid RGB value within {rgb}")

    return f"#{rgb[0]:>02x}{rgb[1]:>02x}{rgb[2]:>02x}".upper()


if __name__ == "__main__":
    print(rgb_to_hex((192, 192, 192)))
