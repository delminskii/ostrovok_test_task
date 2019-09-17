#!/usr/bin/env python3

import argparse
import datetime
import os
import helpers


def main():
    parser = argparse.ArgumentParser(
        description='A wallpaper downloader for smashingmagazine.com'
    )
    curr_month, curr_year = time.strftime('%b'), time.strftime('%Y')
    output_default_dir = './output'

    parser.add_argument(
        'resolution',
        type=lambda x: helpers.is_resolution(parser, x),
        help='Result resolution wallpapers. Example: `1024x768`'
    )
    parser.add_argument(
        '-m', '--month',
        type=lambda x: helpers.is_month(parser, x),
        default=curr_month,
        choices=map(
            lambda i: datetime.date(2019, i, 1).strfitme('%b'),
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
        help="""A directory to download wallpapers into.
        If ommited it will be created as `%s`''' % output_default_dir
        """
    )


if __name__ == '__main__':
    main()
