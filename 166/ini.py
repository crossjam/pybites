import configparser
import re

cookiecutter = """[tox]
envlist = py27, py34, py35, py36, pypy, flake8

[testenv]
passenv = LC_ALL, LANG, HOME
commands = pytest --cov=cookiecutter {posargs:tests}
deps = -rtest_requirements.txt

[testenv:flake8]
deps =
    flake8==3.5.0
commands =
    flake8 cookiecutter tests setup.py

[testenv:cov-report]
commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""

        self.config = configparser.ConfigParser()
        if isinstance(ini_file, str):
            self.config.read_string(ini_file)
        else:
            self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
        New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
        (= "envlist" attribute of [tox] section)"""
        if "tox" in self.config and "envlist" in self.config["tox"]:
            return sorted(
                {
                    env.strip()
                    for env in re.split(
                        r"[^a-zA-Z0-9_\-]+", self.config["tox"]["envlist"]
                    )
                    if env.strip()
                }
            )
        else:
            return []

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        return {
            section["basepython"].strip()
            for section in self.config.values()
            if "basepython" in section and section["basepython"].strip()
        }


if __name__ == "__main__":
    tox_ini_parser = ToxIniParser(cookiecutter)
    print(tox_ini_parser.number_of_sections)
    print(tox_ini_parser.environments)
    print(tox_ini_parser.base_python_versions)
