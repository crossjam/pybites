import re

from urllib.parse import urlparse


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:
    @classmethod
    def parse_url(klass, url):
        res = urlparse(url)
        return klass(res[1])

    @classmethod
    def parse_email(klass, email):
        uname, domain = email.split("@", 1)
        return klass(domain)

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        m = re.match(r".*\.[a-z]{2,3}$", name)
        if not m:
            raise DomainException(f"Invalid domain: {name}")
        self.name = name

    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    def __str__(self):
        return self.name


if __name__ == "__main__":
    print(Domain("google.com"))
    print(Domain("nu.nl"))
    print(Domain.parse_url("https://python.org/"))
    print(Domain.parse_email("foo@example.com"))
    print(Domain("nu.nlll"))
