#!/usr/bin/env python3

import argparse
import datetime
import os
import helpers


def main():
    parser = argparse.ArgumentParser(
        description='A wallpaper downloader for smashingmagazine.com'
    )

    curr_month = datetime.datetime.now().strftime('%b')
    curr_year = datetime.datetime.now().strftime('%Y')
    output_default_dir = './output'

    # months = [datetime.date(2019, m, 1).strftime('%b') for m in range(1, 13)]
    # print(months)

    parser.add_argument(
        'resolution',
        type=lambda x: helpers.is_resolution(parser, x),
        help='Result resolution wallpapers. Example: `1024x768`'
    )
    parser.add_argument(
        '-m', '--month',
        type=str,
        default=curr_month,
        choices=map(
            lambda m: datetime.date(2019, m, 1).strftime('%b'),
            range(1, 13)
        ),
        help='A month to download wallpapers for. Example: `Jan` or `Dec`'
    )
    parser.add_argument(
        '-y', '--year',
        type=lambda x: helpers.is_year(parser, x),
        default=curr_year,
        help='A year to download wallpapers for. Example: `2012` or `2000`'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=os.path.join(os.getcwd(), output_default_dir),
        help='''
        A directory to download wallpapers into.
        If ommited it will be created as `%s`
        ''' % output_default_dir
    )
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
