#!/usr/bin/env python3

import re


def is_resolution(parser, resolution_str, pattern=r'\d+x\d+'):
    """check whether resolution_str string fits good to normal image resolution

    :param parser: argparse parser object
    :param resolution_str: source string for resolution. Example: 1600x900
    :param pattern: regexp pattern whether to match resolution_str string
    """
    if re.match(pattern, resolution_str) is None:
        parser.error(f'{resolution_str} does not fit good to image resolution')
    return resolution_str.lower()
    # return bool(re.match(pattern, resolution_str))


def is_month(parser, month_str):
    month_str = month_str.lower()
    possible_months = (
        'Jan', 'Feb', 'Mar', 'Apr',
        'May', 'Jun', 'Jul', 'Aug',
        'Sep', 'Oct', 'Nov', 'Dec'
    )
    # TODO


def is_year(parser, year_str, pattern=r'[12]\d{3}'):
    """check whether year_str fits good to year pattern (format: YYYY)

    :param parser: argparse parser object
    :param year_str: source string for year. Example: 2012
    :param pattern: regexp pattern while to match year_str string
    """
    # TODO
    pass
