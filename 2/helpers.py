#!/usr/bin/env python3

import re


def is_resolution(parser, resolution_str, pattern=r'\d+x\d+'):
    """check whether resolution_str string fits good to normal image resolution

    :param parser: argparse parser object
    :param resolution_str: source string for resolution. Example: 1600x900
    :param pattern: regexp pattern whether to match resolution_str string
    """
    if re.match(pattern, resolution_str) is None:
        parser.error(
            f"`{resolution_str}` does not fit good to image resolution"
        )
    return resolution_str.lower()


def is_year(parser, year_str, pattern=r'[12]\d{3}'):
    """check whether year_str fits good to year pattern (format: YYYY)

    :param parser: argparse parser object
    :param year_str: source string for year. Example: 2012
    :param pattern: regexp pattern while to match year_str string
    """
    if re.match(pattern, year_str) is None:
        parser.error(f"`{year_str}` does not fit good to year in YYYY format")
    return year_str
