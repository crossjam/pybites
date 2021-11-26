import re


VALID_LICENSE_RGX = re.compile(r"^PB(-[A-Z0-9]{8}){4}$")


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
    (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """

    return VALID_LICENSE_RGX.match(key) is not None


if __name__ == "__main__":
    print(validate_license("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"))
