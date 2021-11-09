from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie"""

    pass


def _maybe_DateFormats(date_str):
    """Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(
                date_str, d_parse_fmt
            )  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Allowed/supported date formats are defined in a DF enum class.
    """
    # complete this method

    maybe_results = []
    for date in dates:
        maybe_results.extend(_maybe_DateFormats(date))

    counter = Counter(maybe_results)
    unique_counts = set(counter.items())

    top_2 = counter.most_common(2)

    if top_2[0][1] == top_2[1][1]:
        raise InfDateFmtError

    date_format_enum = top_2[0][0]

    if date_format_enum == DateFormat.NONPARSABLE:
        raise InfDateFmtError

    date_format = DateFormat.get_d_parse_formats()[date_format_enum.value]

    res = []
    for date in dates:
        try:
            _parsed_date = datetime.strptime(date, date_format)  # pylint: disable=W0612
            res.append(_parsed_date.strftime("%Y-%m-%d"))
        except ValueError:
            res.append("Invalid")
    return res


if __name__ == "__main__":
    DATES = [
        "12/16/30",
        "16/03/54",
        "97/07/26",
        "04/04/31",
        "01/08/07",
        "02/02/29",
        "73/03/08",
        "06/07/55",
        "10/09/77",
        "18/03/43",
        "30/11/24",
        "08/01/51",
    ]
    print(get_dates(DATES))
